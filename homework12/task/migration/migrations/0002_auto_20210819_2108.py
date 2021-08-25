# Generated by Django 3.2.6 on 2021-08-19 21:08
import datetime

from django.db import migrations


def add_row(apps, schema_editor):
    Teacher = apps.get_model("migration", "Teacher")
    t = Teacher(first_name="Ivan", last_name="Wonderful")
    t.save()

    Student = apps.get_model("migration", "Student")
    st = Student(first_name="Olya", last_name="Yalo")
    st.save()

    Homework = apps.get_model("migration", "Homework")
    hw = Homework(
        text="Calculate integral", deadline=datetime.timedelta(days=7), teacher=t
    )
    hw.save()

    HomeworkResult = apps.get_model("migration", "HomeworkResult")
    hw_result = HomeworkResult(hw=hw, solution="Done", student=st)
    hw_result.save()


class Migration(migrations.Migration):

    dependencies = [
        ("migration", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(add_row),
    ]
