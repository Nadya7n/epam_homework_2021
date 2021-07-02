from itertools import product
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    return [list(i) for i in product(*args)]
