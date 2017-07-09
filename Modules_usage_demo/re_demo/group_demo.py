# -*- encoding: utf-8 -*-

import re
m = re.match(r"(..)+", "a1b2c3") # Matches 3 times.
m.group()
# "a1b2c3"
m.group(1)
# "c3', 一个group的每一次匹配覆盖上一次的匹配结果