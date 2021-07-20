import datetime

import pytest

from homework5 import oop_1


def test_class_homework():
    """
    Testing that attributes and method of Class Homework work correct
    """
    homework_1 = oop_1.Homework("Maths", 5)
    homework_2 = oop_1.Homework("Statistics", 0)
    text_1, deadline_1 = homework_1.text, homework_1.deadline
    text_2, deadline_2 = homework_2.text, homework_2.deadline
    assert text_1 == "Maths"
    assert deadline_1 == datetime.timedelta(days=5)
    assert text_2 == "Statistics"
    assert deadline_2 == datetime.timedelta(0)


def test_class_student():
    """
    Testing that attributes and method of Class Student work correct
    """
    student = oop_1.Student("Ivanov", "Ivan")
    homework_1 = oop_1.Homework("Maths", 5)
    homework_2 = oop_1.Homework("Statistics", 0)
    last_name = student.last_name
    do_hw_1 = student.do_homework(homework_1)
    do_hw_2 = student.do_homework(homework_2)
    assert last_name == "Ivanov"
    assert do_hw_1 is True
    assert do_hw_2 is None


def test_class_teacher():
    """
    Testing that attributes and method of Class Teacher work correct
    """
    teacher = oop_1.Teacher("Smirnov", "Lev")
    first_name = teacher.first_name
    create_hw_1 = teacher.create_homework("Maths", 5).deadline
    create_hw_2 = teacher.create_homework("Statistics", 0).deadline
    assert first_name == "Lev"
    assert create_hw_1 == datetime.timedelta(days=5)
    assert create_hw_2 == datetime.timedelta(0)
