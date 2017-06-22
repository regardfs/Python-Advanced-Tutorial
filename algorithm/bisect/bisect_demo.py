from bisect import *

# Locate the insertion point for x in a to maintain sorted order.
# The parameters lo and hi may be used to specify a subset of the list which should be considered; by default the entire
#  list is used. If x is already present in a, the insertion point will be before (to the left of) any existing entries.
# The return value is suitable for use as the first parameter to list.insert() assuming that a is already sorted.
# The returned insertion point i partitions the array a into two halves so that all(val < x for val in a[lo:i]) for the
# left side and all(val >= x for val in a[i:hi]) for the right side.

# bisect.bisect_left(a, x, lo=0, hi=len(a)) equals to
# bisect.bisect(a, x, lo=0, hi=len(a))

# bisect.bisect_right(a, x, lo=0, hi=len(a))

# bisect.insort_left(a, x, lo=0, hi=len(a)) equals to
# bisect.insort(a, x, lo=0, hi=len(a)))

# bisect.insort_right(a, x, lo=0 hi=len(a))

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect(breakpoints, score)
    return grades[i]

[grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]


data = [('red', 5), ('blue', 1), ('yellow', 8), ('black', 0)]
data.sort(key=lambda r: r[1])
keys = [r[1] for r in data]         # precomputed list of keys
data[bisect_left(keys, 0)]

data[bisect_left(keys, 1)]

data[bisect_left(keys, 5)]

data[bisect_left(keys, 8)]