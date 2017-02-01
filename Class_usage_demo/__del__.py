"""
https://docs.python.org/3/reference/datamodel.html#object.__del__
"""

# del x doesn’t directly call x.__del__():
# — the former decrements the reference count for x by one,
# - the latter is only called when x‘s reference count reaches zero.


class NewClass(object):

    num_count = 0

    def __init__(self, name):
        self.name = name
        self.__class__.num_count += 1
        print name, NewClass.num_count

    def __del__(self):
        self.__class__.num_count -= 1
        print "Del", self.name, self.__class__.num_count

    @staticmethod
    def test():
        print "aa"


aa = NewClass("Hello")
bb = NewClass("World")
cc = NewClass("aaaa")

print "Over"


