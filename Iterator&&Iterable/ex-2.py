# file operate islice or readlines

from itertools import islice

# Docstring:
# islice(iterable, [start,] stop [, step]) --> islice object

# get 100 to 300th lines
with open("test.log", "a+") as f:
    islice(f, 100, 300)

# islice will consumed the filtered or iterator items

l = [x for x in xrange(30)]
i = iter(l)

# 0 - 14
for x in islice(i,0,15):
    print x

# 15 - 29
for x in i:
    print x

# get 0 to 500
islice(f, 500) # Attention, f only remain lines start at 500!

# get 500 to end
islice(f, 500, None)


