__version__ = "0.1.0"

from abc import ABC, abstractmethod


class Puggle:
    def __init__(self, name="unknown"):
        self.name = name


class Dog:
    def __init__(self, name="unknown"):
        self.name = name

    def greet(self):
        return f"Hmm. Why am I even being called? I really want each breed to do this."

    def sleep(self):
        return "zzz"


# class Dog(ABC):
#     def __init__(self, name="unknown"):
#         self.name = name

#     @abstractmethod
#     def greet(self):
#         pass

#     def sleep(self):
#         return "zzz"


class Puggle(Dog):

    count = 0

    def __init__(self, name="unknown"):
        super().__init__(name)
        Puggle.count += 1

        # alternate syntax
        # self.__class__.count += 1

    @classmethod
    def get_breed_count(cls):
        return cls.count

    @staticmethod
    def get_characteristics():
        return "Like a mini boxer"

    def greet(self):
        return f"I am {self.name}. I am SO HAPPY to meet you!"


class Boxer(Dog):
    def greet(self):
        return f"The name's {self.name}. Pleasure."
