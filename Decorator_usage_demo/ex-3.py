# decorator with arguments

# python 3
from inspect import signature


def type_assert(*tp_args, **tp_kargs):
    def decorator(func):
        sig = signature(func)
        b_types = sig.bind_partial(*tp_args, **tp_kargs).arguments()

        def wrapper(*args, **kargs):
            for name, obj in sig.bind(*args, **kargs).arguments():
                if name in b_types:
                    if not isinstance(obj, b_types[name]):
                        raise TypeError("TypeError!")
            return func(*args, **kargs)

        return wrapper
    return decorator


# python 2

