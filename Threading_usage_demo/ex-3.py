# Thread Pool

from concurrent.futures import ThreadPoolExecutor

thp = ThreadPoolExecutor(4)


# submit
def f(a, b):
    print 'f', a, b
    return a+b

f = thp.submit(f, 2, 3)

f.result()

# map return a generator(next() to get item)

thp.map(f, [1, 2, 3], [4, 5, 6])

