# -*- encoding: utf-8 -*-
# Using partial to use a 2-argument function where a 1-argument calla‐ ble is required.
# partial冻结参数！！！
from operator import mul
from functools import partial

triple = partial(mul, 3)

triple(7)

list(map(triple, range(1, 10)))