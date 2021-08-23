import datetime

import pytest

from homework5 import oop_1


@pytest.fixture()
def sample_for_test():
    """
    Pull of sample data for test
    :return: 2 objects of class Homework, object of class Student and Teacher
    """
    student = oop_1.Student("Ivanov", "Ivan")
    teacher = oop_1.Teacher("Smirnov", "Lev")
    homework_1 = oop_1.Homework("Maths", 5)
    homework_2 = oop_1.Homework("Statistics", 0)
    return homework_1, homework_2, student, teacher


def test_class_homework(sample_for_test):
    """
    Testing that attributes and method of Class Homework work correct
    """
    homework_1, homework_2, _, _ = sample_for_test
    assert homework_1.text == "Maths"
    assert homework_1.deadline == datetime.timedelta(days=5)
    assert homework_2.text == "Statistics"
    assert homework_2.deadline == datetime.timedelta(0)
    assert homework_1.is_active() is True
    assert homework_2.is_active() is False


def test_class_student(sample_for_test):
    """
    Testing that attributes and method of Class Student work correct
    """
    homework_1, homework_2, student, _ = sample_for_test
    do_hw_1 = student.do_homework(homework_1)
    do_hw_2 = student.do_homework(homework_2)
    assert student.last_name == "Ivanov"
    assert isinstance(do_hw_1, oop_1.Homework)
    assert do_hw_2 is None


def test_class_teacher(sample_for_test):
    """
    Testing that attributes and method of Class Teacher work correct
    """
    _, _, _, teacher = sample_for_test
    create_hw_1 = teacher.create_homework("Maths", 5).deadline
    create_hw_2 = teacher.create_homework("Statistics", 0).deadline
    assert teacher.first_name == "Lev"
    assert create_hw_1 == datetime.timedelta(days=5)
    assert create_hw_2 == datetime.timedelta(0)
