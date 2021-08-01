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


# решение проблемы, когда в дереве есть и 1, и True
def flags_for_bool_int(s_element):
    """
    Assigns flags for searching element bool or int
    :param s_element: element searched for in tree
    :return: int_flag and bool_flag
    """
    int_flag = True if type(s_element) == int else False
    bool_flag = True if type(s_element) == bool else False
    return int_flag, bool_flag


def check_flags(el, s_elem, counter):
    """
    Check flags and type of found in tree element
    if flag and type equal increment the counter once
    :param el: found in tree element
    :param s_elem: element searched for in tree
    :param counter: counter of found elements
    :return: counter
    """
    int_flag, bool_flag = flags_for_bool_int(s_elem)
    if (type(el) == int and int_flag) or (type(el) == bool and bool_flag):
        counter += 1
    elif not bool_flag and not int_flag:
        counter += 1
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
        if el == s_element:
            counter = check_flags(el, s_element, counter)
        if isinstance(el, list) or isinstance(el, tuple) or isinstance(el, set):
            counter = list_tuple_set_mode(el, s_element, counter)
        elif isinstance(el, dict):
            counter = dict_mode(el, s_element, counter)
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
        if key == s_element:
            counter = check_flags(key, s_element, counter)
        if value == s_element:
            counter = check_flags(value, s_element, counter)
        if (
            isinstance(value, list)
            or isinstance(value, tuple)
            or isinstance(value, set)
        ):
            counter = list_tuple_set_mode(value, s_element, counter)
        elif isinstance(value, dict):
            counter = dict_mode(value, s_element, counter)
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
