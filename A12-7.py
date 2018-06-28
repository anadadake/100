import os
import pickle


class Celsius:
    def __init__(self, value=26.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, key, value):
        self.value = float(value)


class Fahrenheit:
    def __get__(self, instance, owner):
        return instance.cel * 1.8 + 32

    def __set__(self, instance, value):
        instance.cel = (float(value) - 32) / 1.8


class Temperature:
    cel = Celsius()
    fah = Fahrenheit()


if __name__ == '__main__':
    temp = Temperature()
    print(temp.cel)
    print(temp.fah)
    temp.cel = 30
    print(temp.fah)

    a = [ i for i in range(100) if  i % 3]
    print (list(a))
