from abc import ABC, abstractmethod


class Dog(ABC):

    count = 0

    def __init__(self, name="unknown"):
        self.name = name
        self.__some_private_concern = "????"
        Dog.count += 1
        # self.__class__.count += 1

    @abstractmethod
    def greet(self):
        return "???????"

    def sleep(self):
        return "zzz"

    @classmethod
    def get_dog_count(cls):
        return f"The number of dogs created is {cls.count}"

    def __repr__(self):
        return f"{self.__class__.__name__} instance."


class Puggle(Dog):
    def __str__(self):
        return f"I am a Puggle named {self.name}"

    def greet(self):
        return "I am SO happy to see you!!!"

    @staticmethod
    def get_characteristics():
        return "Mix of pug and beagle. Looks like a min boxer."


class Boxer(Dog):
    def greet(self):
        return "Howdy, how's it going?"

    def sleep(self):
        return "snore"


class Mutt(Dog):
    def greet(self):
        return "I'm a bunch of breeds"


if __name__ == "__main__":
    lela = Puggle()
    # print(lela)
    print(repr(lela))

    marv = Boxer()
    print(repr(marv))
