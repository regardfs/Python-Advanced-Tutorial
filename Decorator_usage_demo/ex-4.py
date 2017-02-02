# calculate run time whether larger than time limit
# set timeout argument number when function calling

from functools import wraps
from random import randint
import time
import logging


def warn(timeout):
    timeout = [timeout]

    def decorator(func):
        def wrapper(*args, **kwargs):
            start_tm = time.time()
            res = func(*args, **kwargs)
            end_tm = time.time()
            used_time = end_tm - start_tm
            if used_time > timeout[0]:
                msg = "%s run time %s larger than %s" % (func.__name__, used_time, timeout[0])
                logging.warn(msg)
            return res

        def settimeout(tm):
            timeout[0] = tm    # python3: use ```nonlocal timeout```
        wrapper.settimeout = settimeout
        return wrapper
    return decorator


@warn(1.5)
def fun():
    print "testing"
    while randint(0,1):
        time.sleep(randint(0, 2))


# set timeout by wrapper function settimeout
fun.settimeout(1)
for _ in xrange(10):
    fun()

