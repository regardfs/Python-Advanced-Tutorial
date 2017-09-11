# -*- encoding: utf-8 -*-# set

l = [1,2,2,3,3,1,2,3,2]
set(l)
p = [1]
len(set(l)&set(p))
# better way
len(set(l).intersection(set(p)))
# set pop
set(l).pop()
# 集合推导