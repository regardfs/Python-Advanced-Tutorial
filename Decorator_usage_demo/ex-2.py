# keep function metadata when using closure
# f.__name__
# f.__doc__
# f.__module__
# f.__dict__
# f.__defaults__
# ...

from functools import wraps


def cache(func):

    cache_dir = {}

    @wraps(func)
    def warp(*args):
        if args not in cache_dir:
            cache_dir[args] = func(*args)
        return cache_dir[args]

    return warp






