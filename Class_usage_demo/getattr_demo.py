"""

getattr(object, name[, default])

Return the value of the named attribute of object. name must be a string.
If the string is the name of one of the object’s attributes, the result is the value of that attribute.
For example, getattr(x, ‘foobar’) is equivalent to x.foobar.
If the named attribute does not exist, default is returned if provided, otherwise AttributeError is raised.

"""


class Fengshuo:

    def __init__(self):
        self.name = 'Fengshuo'

    def set_name(self, name):
        self.name = name

    def get_name(self):

        return self.name

    def greet(self):

        print "Hello: %s" % self.name

foo = Fengshuo()

hasattr(foo, "name")
# use getattr to execute a function
getattr(foo, "set_name")("leo")
getattr(foo, "name", "N/A")
