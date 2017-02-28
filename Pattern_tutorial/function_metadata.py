# metadata for function


def func(a=1, b=[], c=None):
    """
    :param a:
    :param b:
    :param c:
    :return:
    """
    a = 1
    b = [1]
    c = {'a':a, 'b': b}
    print(a, b, c)
"""
func.__annotations__  func.__defaults__     func.__eq__           func.__globals__      func.__le__           func.__new__
func.__call__         func.__delattr__      func.__format__       func.__gt__           func.__lt__           func.__qualname__
func.__class__        func.__dict__         func.__ge__           func.__hash__         func.__module__       func.__reduce__
func.__closure__      func.__dir__          func.__get__          func.__init__         func.__name__         func.__reduce_ex__
func.__code__         func.__doc__          func.__getattribute__ func.__kwdefaults__   func.__ne__           func.__repr__
"""