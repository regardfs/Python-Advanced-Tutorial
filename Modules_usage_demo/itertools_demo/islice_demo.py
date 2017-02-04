"""
def islice(iterable, *args):
    #  --> A B
    # islice('ABCDEFG', 2, 4) --> C D
    # islice('ABCDEFG', 2, None) --> C D E F G
    # islice('ABCDEFG', 0, None, 2) --> A C E G
    s = slice(*args)
    it = iter(xrange(s.start or 0, s.stop or sys.maxint, s.step or 1))
    nexti = next(it)
    for i, element in enumerate(iterable):
        if i == nexti:
            yield element
            nexti = next(it)
"""

from itertools import islice, count


print 'Stop at 5:'
for i in islice(count(), 5):
    print i

print 'Start at 5, Stop at 10:'
for i in islice(count(), 5, 10):
    print i

print 'By tens to 100:'
for i in islice(count(), 0, 100, 10):
    print i

# Stop at 5:
# 0
# 1
# 2
# 3
# 4
# Start at 5, Stop at 10:
# 5
# 6
# 7
# 8
# 9
# By tens to 100:
# 0
# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80
# 90