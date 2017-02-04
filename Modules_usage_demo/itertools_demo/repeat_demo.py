"""
def repeat(object, times=None):
    # repeat(10, 3) --> 10 10 10
    if times is None:
        while True:
            yield object
    else:
        for i in xrange(times):
            yield object
"""

from itertools import repeat

for i in repeat('over-and-over', 5):
    print i
    
"""
over-and-over
over-and-over
over-and-over
over-and-over
over-and-over
"""