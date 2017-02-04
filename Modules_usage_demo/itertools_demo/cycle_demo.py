"""
def cycle(iterable):
    # cycle('ABCD') --> A B C D A B C D A B C D ...
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
              yield element

"""

from itertools import cycle

# A B C D A B C D A B C D ...
cycle('ABCD')

"""
(1, 'a')
(2, 'b')
(3, 'c')
(4, 'a')
(5, 'b')
(6, 'c')
(7, 'a')
(8, 'b')
(9, 'c')
"""
i = 0
for item in cycle(['a', 'b', 'c']):
    i += 1
    if i == 10:
        break
    print (i, item)