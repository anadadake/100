import os
import pickle

class C:
    def __init__(self):
        self.x = 'X-man'

class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __setattr__(self, name, value):
        if name == 'square':
            self.width = value
            self.height = value
        else:
            super.__setattr__(self,name,value)

    def getArea(self):
        return self.width * self.height


if __name__ == '__main__':
    r1 = Rectangle(4, 5)
    print(r1.getArea())


    r1.square  = 10

    print(r1.getArea())
    # c= C()
    # # print(c.x)
    # print(getattr(c,'x','no this x proerties'))
    #
    #
    #
    # setattr(c,'y','y value')
    # print(getattr(c, 'y', 'no this y proerties'))
