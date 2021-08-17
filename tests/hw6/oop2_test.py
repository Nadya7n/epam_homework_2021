import pytest
from unittest import TestCase

from homework6 import oop_2


def test_all_cases():
    opp_teacher = oop_2.Teacher("Daniil", "Shadrin")
    advanced_python_teacher = oop_2.Teacher("Aleksandr", "Smetanin")

    lazy_student = oop_2.Student("Roman", "Petrov")
    good_student = oop_2.Student("Lev", "Sokolov")

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)

    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    assert result_1.solution == "I have done this hw"
    result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
    assert result_2.homework.text == "Read docs"
    result_3 = lazy_student.do_homework(docs_hw, "done")
    assert result_3.author.last_name == "Petrov"

    with TestCase.assertRaises(TestCase, expected_exception=AttributeError):
        oop_2.HomeworkResult(good_student, "fff", "Solution")

    assert opp_teacher.check_homework(result_1) is True
    assert advanced_python_teacher.check_homework(result_1) is True

    temp_1 = opp_teacher.homework_done
    temp_2 = oop_2.Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    assert len(opp_teacher.homework_done) == 2
    opp_teacher.reset_results(docs_hw)
    assert len(opp_teacher.homework_done) == 1

    assert oop_2.Teacher.homework_done[oop_hw] == {"I have done this hw"}
    assert oop_2.Teacher.reset_results() is None
