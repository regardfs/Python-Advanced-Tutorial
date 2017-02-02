from random import choice
import time

def f():
    print "in f"


def g():
    print "in g"


def h():
    print "in h"

for _ in xrange(50):
    choice([f, g, h])()
    time.sleep(choice([1, 2, 3]))

