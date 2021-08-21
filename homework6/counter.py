"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""
import functools


def instances_counter(cls):
    """
    Decorator of class
    :param cls:
    :return: methods get_created_instances, reset_instances_counter
    """

    @classmethod
    def init_counter(cls):
        if "created_instances" not in cls.__dict__:
            cls.created_instances = 0

    original_init = cls.__init__

    @functools.wraps(original_init)
    def new_init(self, *args, **kwargs):
        self.__class__.init_counter()
        self.__class__.created_instances += 1
        return original_init(self, *args, **kwargs)

    @classmethod
    def get_created_instances(cls):
        cls.init_counter()
        return cls.created_instances

    @classmethod
    def reset_instances_counter(cls):
        cls.init_counter()
        try:
            return cls.created_instances
        finally:
            cls.created_instances = 0

    cls.__init__ = new_init
    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter
    cls.init_counter = init_counter

    return cls
