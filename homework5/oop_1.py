"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime

1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истекло ли время на выполнение задания,
    возвращает boolean

2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None

3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime


class Homework:
    """
    Homework takes two attributes: task's text and number of days for performing task

    Attributes:
        text - task's text
        deadline - stores a datetime.timedelta object with the number of
    days to execute
        created - with date and time of creation

    Method:
        is_active - check deadline and return boolean
    """

    def __init__(self, text, deadline, created=datetime.datetime.now()):
        self.text = text
        self.deadline = datetime.timedelta(deadline)
        self.created = datetime.datetime.now()

    def is_active(self):
        time_now = datetime.datetime.now()
        time_deadline = self.created + self.deadline
        return False if time_now >= time_deadline else True


class Student:
    """
    Student takes two attributes: last_name and first_name

    Attributes:
        last_name
        first_name

    Method:
        do_homework - takes class Homework and check is active homework or not
    """

    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    @classmethod
    def do_homework(cls, instance):
        method_is_active = Homework.is_active(instance)
        if method_is_active is True:
            return method_is_active
        else:
            print("You are late")


class Teacher:
    """
    Teacher takes two attributes: last_name and first_name

    Attributes:
        last_name
        first_name

    Method:
    create_homework - create an instance of Homework
    """

    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def create_homework(text, deadline):
        return Homework(text, deadline)


if __name__ == "__main__":
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")
    teacher.last_name  # Daniil
    student.first_name  # Petrov

    expired_homework = teacher.create_homework("Learn functions", 0)
    expired_homework.created  # Example: 2019-05-26 16:44:30.688762
    expired_homework.deadline  # 0:00:00
    expired_homework.text  # 'Learn functions'

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    oop_homework.deadline  # 5 days, 0:00:00

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late
