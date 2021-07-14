import os
from datetime import datetime

import pytest


def test_slowness_of_slow_calculator():
    t_start = datetime.now()
    path_to_file = os.path.join(
        os.path.dirname(__file__), "../../homework3/task2/calculator.py"
    )
    os.system(f"python3 {path_to_file}")
    t_stop = datetime.now()
    t_delta = t_start - t_stop
    assert t_delta.total_seconds() < 60
