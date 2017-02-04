"""
def dropwhile(predicate, iterable):
    # dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
    iterable = iter(iterable)
    for x in iterable:
        if not predicate(x):
            yield x
            break
    for x in iterable:
        yield x
"""

from itertools import dropwhile
# drop elements from beginning which qualify the function, afterwards, returns every element.
dropwhile(lambda x: x<5, [1, 2, 3, 4, 5, 6, 1, 4, 5, 2, 1131, 3])