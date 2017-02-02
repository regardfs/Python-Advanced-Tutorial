# closure, remember: decorator is clusure


# use this closure to save cache
def cache(func):
    cache_dir = {}

    def warp(*args):
        if args not in cache_dir:
            cache_dir[args] = func(*args)
        return cache_dir[args]

    return warp


@cache
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

fibonacci(10)