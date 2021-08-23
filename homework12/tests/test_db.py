import pytest

from homework12.task.migration.models import *


def test_django_migration(db):
    assert Teacher.obejcts.all().count() == 1
    assert Student.obejcts.all().count() == 1
    assert Homework.obejcts.all().count() == 1
    assert HomeworkResult.obejcts.all().count() == 1
