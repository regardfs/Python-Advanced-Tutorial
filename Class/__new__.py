# __new__ is the real constructor for python class
# __new__ should be created before __init__
# __new__'s parameter should be cls
# __init__'s self is the return of the __new__
# 
# def __new__(cls, *args, **kwargs)


class inttuple(tuple):
    def __new__(cls, iterable):
        g = (x for x in iterable if isinstance(x, int) and x >= 0)
        return super(inttuple, cls).__new__(cls, g)

    def __init__(self, iterable):
        print self
        super(inttuple, self).__init__(iterable)
