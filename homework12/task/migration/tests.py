from django.test import TestCase
from migration.models import *


class ModelsTestCase(TestCase):
    def test_presence(self):
        assert Teacher.objects.all().count() == 1
        assert Student.objects.all().count() == 1
        assert Homework.objects.all().count() == 1
        assert HomeworkResult.objects.all().count() == 1
