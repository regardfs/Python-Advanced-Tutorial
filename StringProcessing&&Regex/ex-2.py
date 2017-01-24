# combine and join strings

# str.__add__(str1, str2)
str1 = 'hello'
str2 = 'world'
str1 + str2

# str.__gt__(str1, str2)
str1 > str2

# str.__lt__(str1, str2)
str1 < str2

# str.join?

",".join([str1, str2])
"".join([str1, str2])

# string format handle
# we could use pprint or ljust/rjust/center
str3 = "hello, world"
# '                  hello, world'
str3.rjust(30)
# 'hello, world                  '
str3.ljust(30)
# '         hello, world         '
str3.center(30)

# furthermore, we could use format
format(str3, '>30')  # rjust
format(str3, '^30')  # center

# station_dict = StationInfoIterator() from ..Iter_Reversed.ex-1 import StationInfoIterator
d = {'zixi': 'ZXS',
     'ziyang': 'ZVY',
     'ziyangbei': 'FYW',
     'zizhong': 'ZZW',
     'zizhongbei': 'WZW',
     'zizhou': 'ZZY',
     'zongxi': 'ZOY',
     'zoucheng': 'ZIK',
     'zunyi': 'ZIW',
     'zuoling': 'ZSN'}

# map(lambda x: len(x), d.keys())
max_left = max(map(lambda x: len(x), d.keys()))
# use format to print as we demand
formatter = "{:<%s} {} {}" % max_left
for k, v in d.iteritems():
    print formatter.format(k, ":", v)
