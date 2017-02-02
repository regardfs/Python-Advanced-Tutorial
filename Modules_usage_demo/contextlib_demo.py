# we could use contextmanager instead of create a class with __enter__, __exit__
# yeild separate the non_exception and exception generator!
# https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/
from contextlib import contextmanager


@contextmanager
def context():
    try:
        yield
    except Exception as e:
        print "with an error (%s)" % e
        raise e
    else:
        print "no error!"

# another example, use contextmanager to decorate all public api in class

import logging

@contextmanager
def logged(klass, logger):
    # recorder
    def _log(f):
        def __log(*args, **kwargs):
            logger(f, args, kwargs)
            return f(*args, **kwargs)

    for attribute in dir(klass):
        if attribute.startswith("_"):
            continue
        element = getattr(klass, attribute)
        setattr(klass, '__logged_%s' % attribute, element)
        setattr(klass, attribute, _log(element))

    yield klass

    for attribute in dir(klass):
        if not attribute.startswith("__logged"):
            continue
        element = getattr(klass, attribute)
        setattr(klass, attribute[len('__logged_'):], element)
        delattr(klass, attribute)


# test part

class One(object):
    def _private(self):
        pass

    def one(self, other):
        self.two()
        other.thing(self)
        self._private()

    def two(self):
        pass


class Two(object):
    def thing(self, other):
        other.two()


calls = []


def called(meth, args, kw):
    calls.append(meth.im_func.func_name)


with logged(One, called):
    one = One()
    two = Two()
    one.one(two)

calls





# Everything before the call to yield is considered the code for __enter__().
# Everything after is the code for __exit__().
# Let's rewrite our File context manager using the decorator approach:

from contextlib import contextmanager

@contextmanager
def open_file(path, mode):
    the_file = open(path, mode)
    yield the_file
    the_file.close()

files = []

for x in range(100000):
    with open_file('foo.txt', 'w') as infile:
        files.append(infile)

for f in files:
    if not f.closed:
        print('not closed')
