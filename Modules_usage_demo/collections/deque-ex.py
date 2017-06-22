# -*- coding: utf-8 -*-
"""
下面这个是一个有趣的例子，主要使用了deque的rotate方法来实现了一个无限循环
的加载动画
methods:
1. rotate()

"""

import sys
import time
from collections import deque

fancy_loading = deque('>--------------------')

while True:
    print '\r%s' % ''.join(fancy_loading),
    fancy_loading.rotate(1)
    sys.stdout.flush()
    time.sleep(0.08)

# Result:

# 一个无尽循环的跑马灯
# ------------->-------

# if we define a deque with certain maxlen, we could use

lines = deque(maxlen=5)

# another example

dq = deque([x for x in range(10)], maxlen=10)

dq
# deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
dq.rotate(1)
# deque([9, 0, 1, 2, 3, 4, 5, 6, 7, 8])
dq.rotate(-1)
# deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
dq.appendleft(-1)
# deque([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
dq.remove(-1)
# deque([0, 1, 2, 3, 4, 5, 6, 7, 8])
dq.extend([9,10,11])
# deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])