import json
import os
import tempfile
from datetime import datetime

import pytest
import requests_mock

from homework10 import stocks_multi

date_now = datetime.today().strftime("%d/%m/%Y")
url_1 = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={date_now}"
text_1 = "<Valute ID='R01235'><Name>Доллар США<Value>73,4721"


def testing_take_ruble_course():
    with requests_mock.Mocker(real_http=True) as m:
        m.register_uri("GET", url_1, text=text_1)
        assert stocks_multi.take_course_of_ruble(url_1) == 73.4721


url_2 = "https://markets.businessinsider.com/index/components/s&p_500?p=11"
text_2 = "<html><body><p>YES</p></body></html>"


def testing_get_soup_from_html():
    answer = "<html><body><p>YES</p></body></html>"
    with requests_mock.Mocker() as m:
        m.register_uri("GET", url_2, text=text_2)
        assert str(stocks_multi.get_soup_from_http(value=11, flag="main")) == answer


url_3 = "https://markets.businessinsider.com/index/components/s&p_500?p=1"
text_3 = "<table class='table table__layout--fixed'><tr><tr><td><a href='/stocks/yum-stock'><td>135.12<td><td><td><td><td><td>35.12 46.10%<td>"


def testing_parsing_main_page():
    with requests_mock.Mocker(real_http=True) as m_2:
        m_2.register_uri("GET", url_1, text=text_1)
        with requests_mock.Mocker(real_http=True) as m:
            m.register_uri("GET", url_3, text=text_3)
            instance = next(stocks_multi.parsing_main_page(1))
            assert instance.price == 9927.55
            assert instance.growth == 46.1
            assert instance.ref == "/stocks/yum-stock"


url_4 = "https://markets.businessinsider.com/stocks/yum-stock"
text_4 = "<title>YUM Stock | YUM!</title><span class='price-section__label'>YUM! Brands Inc. </span><div class='snapshot__data-item'>30.29<div class> P/E Ratio <div class='snapshot__data-item'>88.08<div class> 52 Week Low <div class='snapshot__data-item'>135.39<div class> 52 Week High"


def testing_parsing_individual_page():
    with requests_mock.Mocker(real_http=True) as m_2:
        m_2.register_uri("GET", url_1, text=text_1)
        with requests_mock.Mocker(real_http=True) as m:
            m.register_uri("GET", url_3, text=text_3)
            with requests_mock.Mocker(real_http=True) as m_3:
                m_3.register_uri("GET", url_4, text=text_4)
                instance = next(stocks_multi.parsing_individual_page_company(1))
                assert instance.ticker == "YUM"
                assert instance.name == "YUM! Brands Inc."
                assert instance.p_e_ratio == 30.29
                assert instance.potential_profit == 1.86


@pytest.fixture()
def tmp_files() -> list:
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_list = []
        for i in range(1, 5):
            temp_file = f"{temp_dir}/file{i}.json"
            temp_list.append(temp_file)
        yield temp_list


def test_into_json(tmp_files):
    path_to_example_data = os.path.join(os.path.dirname(__file__), "example_data.json")
    with open(path_to_example_data, "r") as read_file:
        data = json.load(read_file)
        tmp_list = []
        for item in data:
            instance = stocks_multi.Company(
                item["price"],
                item["growth"],
                None,
                name=item["name"],
                ticker=item["code"],
                p_e_ratio=item["P/E"],
                potential_profit=item["potential profit"],
            )
            tmp_list.append(instance)

        path_1, path_2, path_3, path_4 = tmp_files

        stocks_multi.into_json(
            tmp_storage=tmp_list, attr="price", reverse=True, path=path_1
        )
        stocks_multi.into_json(
            tmp_storage=tmp_list, attr="p_e_ratio", reverse=True, path=path_2
        )
        stocks_multi.into_json(
            tmp_storage=tmp_list, attr="growth", reverse=True, path=path_3
        )
        stocks_multi.into_json(
            tmp_storage=tmp_list, attr="potential_profit", reverse=True, path=path_4
        )

        for i, file in enumerate(tmp_files, start=1):
            path_to_correct_data = os.path.join(os.path.dirname(__file__), "answer")
            with open(file) as fh:
                result = json.load(fh)
                with open(f"{path_to_correct_data}/{i}.json") as fh_1:
                    answer = json.load(fh_1)
                assert result == answer
