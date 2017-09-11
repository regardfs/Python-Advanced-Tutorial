# the below example illustrate `MRO` principle


class Base(object):
    def method(self):
        print("Base")

class Base0(Base):
    def method(self):
        print("Base0")

class Base1(Base):
    def method(self):
        print("Base1")

class Base2(Base):
    def method(self):
        print("Base2")


class Base3(Base0, Base1, Base2):
    pass


base = Base3()
# return Base1
base.method()


def L(klass):
    return [k.__name__ for k in klass.__mro__]

# return ['Base3', 'Base1', 'Base2', 'Base', 'object']
L(Base3)