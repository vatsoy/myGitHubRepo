import random
import sys
import os

class Animal:
    __name = ""
    __height = 0
    __weight = 0
    __sound = ""

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def print_name(self):
        print(self.__name)

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_sound(self):
        return self.__sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kg and say {}".format(self.__name, self.__height,
                                                              self.__weight, self.__sound)


cat = Animal('King', 33, 10, 'Meow')

print(cat.toString())

class Dog(Animal):
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog,self).__init__(name, height, weight, sound)   #from the parent class

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    #def toString(self):
    #    return "{} is {} cm tall and {} kg and say {}, the owner is {}".format(self.__name, self.__height, self.__weight, self.__sound, self.__owner)

    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)

tuzik = Dog("Tuzik", 53, 27, 'Ruff', 'Vadim')

print(tuzik.toString())

print("{} is dog's name, and {} is cat's name".format(tuzik.get_name(), cat.get_name()))

class AnimalTesting:
    def get_type(self, any_name):
        any_name.get_type()
    def print_name(self, any_object):
        any_object.print_name()


test_animals = AnimalTesting()
test_animals.get_type(cat)
test_animals.get_type(tuzik)
test_animals.print_name(cat)
test_animals.print_name(tuzik)

tuzik.multiple_sounds()
tuzik.multiple_sounds(4)

cat.print_name()
tuzik.print_name()

