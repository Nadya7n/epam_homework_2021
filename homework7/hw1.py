"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


def cache(value):
    """
    Cache type of searching element
    :param value: bool
    :return: bool cache
    """
    return value


def types(item, flag):
    """
    Return type of item
    :param item: any element
    :param flag: checked type
    :return: boolean
    """
    return type(item) == flag


def check_flags(el, s_elem, counter):
    """
    Check flags and type of found in tree element
    if flag and type equal increment the counter once
    :param el: found in tree element
    :param s_elem: element searched for in tree
    :param counter: counter of found elements
    :return: counter
    """
    int_s_el = cache(types(s_elem, int))
    bool_s_el = cache(types(s_elem, bool))
    if (types(el, int) and int_s_el) or (types(el, bool) and bool_s_el):
        counter += 1
    if not (int_s_el) and not (bool_s_el):
        counter += 1
    return counter


def check_element(element, s_element, counter):
    """
    Template for searching for an element in a list
    :param element: found in tree element
    :param s_element: element searched for in tree
    :param counter: counter of found elements
    :return: counter
    """
    if element == s_element:
        counter = check_flags(element, s_element, counter)

    if isinstance(element, dict):
        counter = dict_mode(element, s_element, counter)
    elif isinstance(element, (list, tuple, set)):
        counter = list_tuple_set_mode(element, s_element, counter)

    return counter


def list_tuple_set_mode(obj, s_element, counter):
    """
    Searches for an element in a list or tuple or set structure
    :param obj: list or tuple or set structure
    :param s_element: element searched for in tree
    :param counter: counter of found elements
    :return: counter
    """
    for el in obj:
        counter = check_element(el, s_element, counter)
    return counter


def dict_mode(obj, s_element, counter):
    """
    Searches for an element in a dict structure
    :param obj: dict structure
    :param s_element: element searched for in tree
    :param counter: counter of found elements
    :return: counter
    """
    for key, value in obj.items():
        counter = check_element(key, s_element, counter)
        counter = check_element(value, s_element, counter)
    return counter


def find_occurrences(tree: dict, element: Any) -> int:
    """
    Function that combines searches for element across underlying structures in tree
    :param tree: dict that contain many different complex structures
    :param element: element searched for in tree
    :return: int, how many times does the element searched for appear in the tree
    """
    counter = 0
    counter = dict_mode(tree, element, counter)
    return counter


if __name__ == "__main__":
    print(find_occurrences(example_tree, "RED"))  # 6
