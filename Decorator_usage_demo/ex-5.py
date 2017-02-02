# define decorator in class
# use logging

import logging
from time import localtime, time, strftime, sleep
from random import choice


class CallingInfo(object):

    def __init__(self, name):
        log = logging.getLogger(name)
        log.setLevel(logging.INFO)
        fh = logging.FileHandler(name + ".log")
        log.addHandler(fh)
        log.info("Start".center(40, "-"))
        self.log = log
        self.formatter = "%(func)s -> [%(time)s - %(used)s - %(ncalls)s]"

    # decorator function
    def info(self, func):
        def wrapper(*args, **kwargs):
            wrapper.ncalls += 1
            lt = localtime()
            st = time()
            res = func(*args, **kwargs)
            used = time() - st
            info = {}
            info['func'] = func.__name__
            info['time'] = strftime("%x %X", lt)
            info['used'] = used
            info['ncalls'] = wrapper.ncalls
            msg = self.formatter % info
            self.log.info(msg)
            return res

        wrapper.ncalls = 0

        return wrapper

    def set_formatter(self, formatter):
        self.formatter = formatter

    def set_loglevel(self, new_level):
        self.log.setLevel(new_level)

cinfo1 = CallingInfo("mylog1")
cinfo2 = CallingInfo("mylog1")


@cinfo1.info
def f():
    print "in f"


@cinfo1.info
def g():
    print "in g"


@cinfo2.info
def h():
    print "in h"


for _ in xrange(50):
    choice([f, g, h])()
    sleep(choice([1, 2, 3]))

