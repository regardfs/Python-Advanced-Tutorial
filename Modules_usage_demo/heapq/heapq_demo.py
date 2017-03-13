#! /usr/bin/evn python
#coding:utf-8
"""
# heappush() heapq.heappush(heap, item): 将item压入到堆数组heap中。如果不进行此步操作，后面的heappop()失效
# heapq.heappop(heap): 从堆数组heap中取出最小的值，并返回
# heapq.heapify(x): x必须是list，此函数将list变成堆，实时操作。从而能够在任何情况下使用堆的函数
# heapq.merge(*iterables)
"""

from heapq import *


def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h,value)
    return [heappop(h) for i in range(len(h))]

if __name__=="__main__":
    print heapsort([1,3,5,9,2])


h=[]
from heapq import *
h #[]
heappush(h,5)
heappush(h,2)
heappush(h,4)
heappush(h,9)

h #[2, 4, 5, 9]
heappop(h) #2

heappushpop(h,4) # equal to heappush(h,4),heappop(h)

heapify(list())

a=[2,4,6]
b=[1,3,5]
c=merge(a,b)
list(c) #[1, 2, 3, 4, 5, 6]