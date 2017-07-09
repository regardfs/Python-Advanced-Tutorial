# -*- encoding: utf-8 -*-
# 上述方法有些累赘，利用enumerate()会更加直接和优美：
list1 = ["a", "b", "c", "d"]
for index, item in enumerate(list1):
    print(index, item)
# return
# 0 a
# 1 b
# 2 c
# 3 d

# enumerate还可以接收第二个参数，用于指定索引起始值，如：
list1 = ["a", "b", "c", "d"]
for index, item in enumerate(list1, 1):
    print(index, item)
# return
# 1 a
# 2 b
# 3 c
# 4 d

#  When file is too big to open, use enumerate to open a file and count line numbers
count = -1
for index, line in enumerate(open("a", 'r')):
    count += 1