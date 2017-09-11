# -*- encoding: utf-8 -*-
# 装饰器函数在导入时立刻执行，包裹函数只有在显示调用时才会运行


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

# change dict/list/tuple to object
class obj(object):
    dd = []
    def __init__(self, d):
        for a, b in d.iteritems():
            if isinstance(b, (list, tuple)):
               setattr(self, a, [obj(x) if isinstance(x, dict) else x for x in b])
            else:
               setattr(self, a, obj(b) if isinstance(b, dict) else b)



for serivce_name, service_attrs in service_default_conf_yaml['etcd']['services'][project][service].iteritems():
    print serivce_name, service_attrs

prefix  = "/%s/%s/%s" % ('services', 'aliyun', 'slb')
dd = {}

# print leaf path of a tree
def tree_leaf_path(path_dict, prefix, service_attrs):
    for key, value in service_attrs.iteritems():
        if not isinstance(value, dict):
            path_dict["%s/%s" % (prefix, key)] = value
        else:
            test("%s/%s" % (prefix, key), value)


with open(service_default_conf, "r") as stream:
    service_default_conf_yaml = yaml.safe_load(stream)

