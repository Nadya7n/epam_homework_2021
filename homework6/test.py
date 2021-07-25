from collections import defaultdict
import datetime


class Person:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name


class Homework:
    def __init__(self, text, deadline, created=datetime.datetime.now()):
        self.text = text
        self.deadline = datetime.timedelta(deadline)
        self.created = datetime.datetime.now()

    def is_active(self):
        time_now = datetime.datetime.now()
        time_deadline = self.created + self.deadline
        return False if time_now >= time_deadline else True





teacher = Teacher("Ivanov", "Ivan")
teacher_2 = Teacher("Kolov", "Lev")
hw1 = teacher_2.create_homework("oop", 5)
homework2 = Homework("rop", 1)

teacher.check_homework(hw1, "dokjdfa")
teacher.check_homework(homework2, "djkfa")

teacher.reset_results()

print(Teacher.homework_done)





# Атрибут:
#     homework_done - структура с интерфейсом как в словаря, сюда поподают все
#     HomeworkResult после успешного прохождения check_homework
#     (нужно гаранитровать остутствие повторяющихся результатов по каждому
#     заданию), группировать по экземплярам Homework.
#     Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
# Методы:
#     check_homework - принимает экземпляр HomeworkResult и возвращает True если
#     ответ студента больше 5 символов, так же при успешной проверке добавить в
#     homework_done.
#     Если меньше 5 символов - никуда не добавлять и вернуть False.
#
#     reset_results - если передать экземпряр Homework - удаляет только
#     результаты этого задания из homework_done, если ничего не передавать,
#     то полностью обнулит homework_done.
