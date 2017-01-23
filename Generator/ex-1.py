def function():
    print "return 1"
    yield 1

    print "return 2"
    yield 2

    print "return 3"
    yield 3

    print "return 4"
    yield 4

gen = function()

print gen.__iter__() is gen

# usually, we return like ``yield xx`` in the function of __iter__()
# for example:

class test():
    def __init__(self):
        self.a = [1,2,3,4,5]

    def __iter__(self):
        for x in self.a:
            yield x