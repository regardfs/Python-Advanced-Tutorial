"""
from itertools import combinations

def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indices in permutations(range(n), r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)
"""

# return sorted permutations

from itertools import combinations

combinations('ABCD', 2) # --> AB AC AD BC BD CD

combinations(range(4), 3)   # --> 012 013 023 123