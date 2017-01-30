# weak reference, usually used in circular reference: A <==> B

import weakref


class Data(object):
    def __init__(self, value, owner):
        # weak reference of owner
        self.owner = weakref.ref(owner)
        self.value = value

    def __str__(self):
        return "%s's Data, value is %s" % (self.owner(), self.value)

    def __del__(self):
        print "Data.__del__"


class Node(object):
    def __init__(self, value):
        self.data = Data(value, self)

    def __del__(self):
        print "Node.__dell__"

