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
