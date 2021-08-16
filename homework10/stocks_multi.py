import json
import operator
import os
from datetime import datetime
from multiprocessing import Manager, Process

import bs4 as bs
import requests
from retry import retry


class Company:
    def __init__(
        self,
        price,
        growth,
        ref,
        name=None,
        ticker=None,
        p_e_ratio=99999,
        potential_profit=0,
    ):
        self.price = price
        self.growth = growth
        self.ref = ref
        self.name = name
        self.p_e_ratio = p_e_ratio
        self.ticker = ticker
        self.potential_profit = potential_profit


def take_course_of_ruble(url):
    html_course = requests.get(url)
    soup = bs.BeautifulSoup(html_course.text, "lxml")
    course = float(soup.find(id="R01235").value.text.replace(",", "."))
    return course


@retry((requests.ConnectionError, requests.HTTPError), tries=5)
def get_soup_from_http(value=None, flag=None):
    frame_url_main = "https://markets.businessinsider.com"
    url_main_pages = "/index/components/s&p_500"

    mode = {
        "main": f"{frame_url_main}{url_main_pages}?p={value}",
        "individual": f"{frame_url_main}{value}",
        None: f"{frame_url_main}{url_main_pages}",
    }

    html = requests.get(mode[flag])
    soup = bs.BeautifulSoup(html.text, "lxml")

    return soup


def into_json(tmp_storage: list, attr: str, reverse: bool, path: str):
    tmp_storage.sort(key=operator.attrgetter(attr), reverse=reverse)
    top = tmp_storage[:10]
    tmp_list = []
    with open(path, "w") as write_file:
        for item in top:
            tmp_list.append(
                {
                    "code": item.ticker,
                    "name": item.name,
                    "price": item.price,
                    "P/E": item.p_e_ratio,
                    "growth": item.growth,
                    "potential profit": item.potential_profit,
                },
            )
        json.dump(tmp_list, write_file)


def parsing_main_page(page):
    date_now = datetime.today().strftime("%d/%m/%Y")
    url_cbr = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={date_now}"

    soup_main_page = get_soup_from_http(value=page, flag="main")
    table = soup_main_page.find("table", {"class": "table table__layout--fixed"})

    for row in table.find_all("tr")[1:]:
        company_price = row.find_all("td")[1].text
        company_price = float(company_price.split()[0].replace(",", ""))
        company_price_in_rub = round((company_price * take_course_of_ruble(url_cbr)), 2)

        company_growth = row.find_all("td")[7].text
        company_growth = float(company_growth.split()[1].replace("%", ""))

        ref = row.find("a").get("href")

    yield Company(company_price_in_rub, company_growth, ref)


def parsing_individual_page_company(page):
    for instance in list(parsing_main_page(page)):
        url_instance = instance.ref
        soup_ind_page = get_soup_from_http(value=url_instance, flag="individual")
        ticker_company = soup_ind_page.title.string.split()[0]
        name_company = soup_ind_page.find(
            "span", {"class": "price-section__label"}
        ).text.strip()

        instance.ticker = ticker_company
        instance.name = name_company

        all_values_from_page = soup_ind_page.find_all(
            "div", {"class": "snapshot__data-item"}
        )
        week_low_52 = 0
        for item in all_values_from_page:
            single_value_from_page = item.text.strip()

            if "52 Week High" in single_value_from_page:
                week_high_52 = float(single_value_from_page.split()[0].replace(",", ""))
                instance.potential_profit = round(
                    (week_low_52 / (week_high_52 - week_low_52)), 2
                )

            if "52 Week Low" in single_value_from_page:
                week_low_52 = float(single_value_from_page.split()[0].replace(",", ""))

            if "P/E Ratio" in single_value_from_page:
                p_e_ratio = float(single_value_from_page.split()[0].replace(",", ""))
                instance.p_e_ratio = p_e_ratio

        yield instance


def worker(n, returns):
    for item in list(parsing_individual_page_company(n)):
        returns.append(item)


if __name__ == "__main__":
    manager = Manager()
    return_list = manager.list()
    process_work = []

    soup_count_pages = get_soup_from_http()

    number_pages = soup_count_pages.find(
        "div", {"class": "finando_paging margin-top--small"}
    )
    last_page = int(number_pages.text.strip().split()[-1])

    for number in range(1, last_page + 1):
        proc = Process(target=worker, args=(number, return_list))
        process_work.append(proc)
        proc.start()

    for proc in process_work:
        proc.join()

    main_path = os.path.dirname(__file__)
    into_json(
        return_list,
        attr="price",
        reverse=True,
        path=f"{main_path}/top_most_expensive_stocks.json",
    )
    into_json(
        return_list,
        attr="p_e_ratio",
        reverse=False,
        path=f"{main_path}/top_lowest_pe_ratio.json",
    )
    into_json(
        return_list,
        attr="growth",
        reverse=True,
        path=f"{main_path}/top_highest_growth.json",
    )
    into_json(
        return_list,
        attr="potential_profit",
        reverse=True,
        path=f"{main_path}/top_potentially_profitable.json",
    )
