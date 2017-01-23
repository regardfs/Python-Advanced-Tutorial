# #concurrent iterator with zip on several iterable obhect
# zip could combine several iterable object
a = [x for x in xrange(5)]
b = "xyzmn"
# [(0, 'x'), (1, 'y'), (2, 'z'), (3, 'm'), (4, 'n')]
zip(a, b)

# example zip
from random import randint

chinese_record = [randint(0, 101) for _ in xrange(40)]
math_record = [randint(0, 101) for _ in xrange(40)]
english_record = [randint(0, 101) for _ in xrange(40)]

[ c+m+e for c,m,e in zip(chinese_record, math_record, english_record) ]

# iterator one by one with chain
from itertools import chain

a = [x for x in xrange(5)]
b = "xyzmn"
c = ['10','11','12','13','14']
chain(a, b, c)

# example chain
class1_record = [randint(0, 101) for _ in xrange(20)]
class2_record = [randint(0, 101) for _ in xrange(19)]
class3_record = [randint(0, 101) for _ in xrange(18)]
class4_record = [randint(0, 101) for _ in xrange(21)]
len([x for x in chain(class1_record, class2_record, class3_record, class4_record) if x >=90])
