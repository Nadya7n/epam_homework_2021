import datetime

from django.test import TestCase

from migration.models import *


class ModelsTestCase(TestCase):
    def setUp(self):
        Teacher.objects.create(first_name="Ivan", last_name="Wonderful")

        Student.objects.create(first_name="Olya", last_name="Yalo")

        Homework.objects.create(
            text="Calculate integral", deadline=datetime.timedelta(days=7), teacher_id=1
        )

        HomeworkResult.objects.create(hw_id=1, solution="Done", student_id=1)

    def test_presence(self):
        hw = Homework.objects.get(id=1)
        hw_res = HomeworkResult.objects.get(id=1)
        teacher = Teacher.objects.get(id=1)
        student = Student.objects.get(id=1)

        self.assertEqual(hw.text, "Calculate integral")
        self.assertEqual(hw_res.solution, "Done")
        self.assertEqual(teacher.last_name, "Wonderful")
        self.assertEqual(student.first_name, "Olya")
