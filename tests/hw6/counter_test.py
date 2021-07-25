import pytest
from homework6.counter import instances_counter


def test_correct_work_instances_counter():
    """
    Testing that decorator instances_counter works correct
    :return: None
    """

    @instances_counter
    class User:
        """
        Empty class
        """

        pass

    if __name__ == "__main__":
        assert User.get_created_instances() == 0
        user, _, _ = User(), User(), User()
        assert user.get_created_instances() == 3
        assert user.reset_instances_counter() == 3
        assert user.reset_instances_counter() == 0
