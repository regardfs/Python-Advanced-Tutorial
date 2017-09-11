# we should define functions of __lt__, __gt__, __le__, __ge__, __eq__, __ne__ when we want to compare class object
# -*- encoding: utf-8 -*-
from functools import total_ordering
from abc import ABCMeta, abstractmethod
from math import sqrt

# we only need to define two type of compare function, one is __eq__ and other one could be  __lt__ or __gt__

# 这个装饰器是在python2.7的时候加上的，它是针对某个类如果定义了__lt__、le、gt、__ge__这些方法中的至少一个，使用该装饰器，则会自动的把
# 其他几个比较函数也实现在该类中
@total_ordering
class shape(object):

    @abstractmethod
    def area(self):
        pass

    def __gt__(self, other):
        try:
            if isinstance(other, shape):
                if self.area() > other.area():
                    return True
        except TypeError:
            print "Type Error!!!"

    def __eq__(self, other):
        try:
            if isinstance(other, shape):
                if self.area() == other.area():
                    return True
        except TypeError:
            print "Type Error!!!"


class Circle(shape):

    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return self.radius * 2 * 3.14

    def area(self):
        return self.radius ** 2 * 3.14


class Triangle(shape):

    def __init__(self, a, b ,c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        return round(sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)), 3)



