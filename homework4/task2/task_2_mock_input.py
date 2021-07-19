"""
Write a function that accepts an URL as input
and count how many letters `i` are present in the HTML by this URL.

Write a test that check that your function works.
Test should use Mock instead of real network interactions.

You can use urlopen* or any other network libraries.
In case of any network error raise ValueError("Unreachable {url}).

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - test could be run without internet connection

You will learn:
 - how to test using mocks
 - how to write complex mocks
 - how to raise an exception form mocks
 - do a simple network requests


# >>> count_dots_on_i("https://example.com/")
# 59

* https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
"""
import urllib.request


def check_site(site_name):
    try:
        link = urllib.request.urlopen(site_name)
    except:
        raise ValueError
    else:
        return link


def count_dots_on_i(url: str) -> int:
    counter = 0
    try:
        link = check_site(url)
    except ValueError:
        raise ValueError
    else:
        for line in link.readlines():
            for char in line.decode("utf-8"):
                if char == "i":
                    counter += 1
        return counter
