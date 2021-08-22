from django.test import TestCase

from migration.models import *


class AnimalTestCase(TestCase):
    def test_presence(self):
        hw = Homework.objects.get(text="Calculate integral")
        hw_res = HomeworkResult.objects.get(solution="Done")
        teacher = Teacher.objects.get(last_name="Wonderful")
        student = Student.objects.get(first_name="Olya")

        self.assertEqual(hw.text, "Calculate integral")
        self.assertEqual(hw_res.solution, "Done")
        self.assertEqual(teacher.last_name, "Wonderful")
        self.assertEqual(student.first_name, "Olya")
