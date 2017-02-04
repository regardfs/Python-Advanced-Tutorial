"""
def count(start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step
"""

from itertools import *

for i in izip(count(1), ['a', 'b', 'c']):
    print i

"""
(1, 'a')
(2, 'b')
(3, 'c')
"""
