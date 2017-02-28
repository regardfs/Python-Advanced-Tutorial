# without decorator
def fib(n, cache=None):
    if cache is None:
        cache = {}

    if n in cache:
        return cache[n]

    if n <= 1:
        return 1
    cache[n] = fib(n-2, cache) + fib(n-1, cache)
    return cache[n]

# TEST
fib(50)


# use closure
def cache(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


