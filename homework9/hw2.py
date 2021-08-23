"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

# >>> with suppressor(IndexError):
# ...    [][2]

"""
import contextlib


class Suppressor:
    """
    >>> with Suppressor(IndexError):
    ...    [][2]
    """

    def __init__(self, name_error):
        self.name_error = name_error

    def __enter__(self):
        ...

    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_type == self.name_error


@contextlib.contextmanager
def suppressor(name_error):
    """
    >>> with suppressor(IndexError):
    ...    [][2]
    """
    try:
        yield ...
    except name_error:
        pass
