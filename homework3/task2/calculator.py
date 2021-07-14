"""
Here's a not very efficient calculation function
that calculates something important::

    import time
    import struct
    import random
    import hashlib

    def slow_calculate(value):
        # Some weird voodoo magic calculations
        time.sleep(random.randint(1,3))
        data = hashlib.md5(str(value).encode()).digest()
        return sum(struct.unpack('<' + 'B' * len(data), data))

Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
Calculation time should not take more than a minute.
Use functional capabilities of multiprocessing module.
You are not allowed to modify slow_calculate function.
"""
import hashlib
import random
import struct
import time
from multiprocessing import Manager, Process


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def worker(n, return_l):
    return_l[n] = slow_calculate(n)


if __name__ == "__main__":
    manager = Manager()
    return_dict = manager.dict()
    numbers = [i for i in range(500)]
    process_work = []

    for index, number in enumerate(numbers):
        proc = Process(target=worker, args=(number, return_dict))
        process_work.append(proc)
        proc.start()

    for proc in process_work:
        proc.join()

    print(sum(value for value in return_dict.values()))
