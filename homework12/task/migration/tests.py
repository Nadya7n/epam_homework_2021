from django.test import TestCase
from migration.models import *


class AnimalTestCase(TestCase):
    def test_presence(self):
        hw = Homework.objects.get(pk=1)
        hw_res = HomeworkResult.objects.get(pk=1)
        teacher = Teacher.objects.get(pk=1)
        student = Student.objects.get(pk=1)

        self.assertEqual(hw.text, "Calculate integral")
        self.assertEqual(hw_res.solution, "Done")
        self.assertEqual(teacher.last_name, "Wonderful")
        self.assertEqual(student.first_name, "Olya")
