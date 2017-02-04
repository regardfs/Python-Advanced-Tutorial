"""
def compress(data, selectors):
    # compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
    return (d for d, s in izip(data, selectors) if s)
"""

from itertools import compress

#  A C E F
compress('ABCDEF', [1,0,1,0,1,1])