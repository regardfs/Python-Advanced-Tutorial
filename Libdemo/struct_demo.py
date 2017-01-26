# struct lib
from struct import pack,unpack
# unpack(fmt, string)
# 258, litter-endian
unpack('h', '\x02\01')
# 513, big-endian
unpack('>h', '\x02\01')


