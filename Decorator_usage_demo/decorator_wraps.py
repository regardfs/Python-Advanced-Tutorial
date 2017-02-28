from functools import wraps


def cacher(func):
    cache = {}
    # use wraps to use func metadata
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


@cacher
def fib(n):
    if n <=1:
        return 1
    return fib(n-2) + fib(n-1)
