# use decorator in the scenario of instance as attribute of class


class Decorator(object):
    def __get__(self, instance, owner):
        print "__get__", instance, owner
        # return instance.__dict__[]

    def __set__(self, instance, value):
        print "__set__"
        # instance.__dict__[] == value

    def __delete__(self, instance):
        print "__delete__"
        # del instance.__dict__[]


class Test(object):
    x = Decorator()

t = Test()
# __get__ <__main__.Test object at 0x10ec15b50> <class '__main__.Test'>
t.x
# __set__
t.x = "xyz"
# __delete__
del t.x


# an example
class Attr(object):

    def __init__(self, attr_name, type_):
        self.attr_name = attr_name
        self.type_ = type_

    def __get__(self, instance, owner):
        return instance.__dict__[self.attr_name]

    def __set__(self, instance, value):
        if not isinstance(value, self.type_):
            raise TypeError("Type Error, expect %s", self.type_)

    def __delete__(self, instance):
        del instance.__dict__[self.attr_name]


class Student(object):

    def __init__(self, name, grade, class_name):
        self.name = Attr(name, str)
        self.grade = Attr(grade, int)
        self.class_name = Attr(class_name, int)



