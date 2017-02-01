# use file.seek(offset, whence=0) to fix position
# whence: 0: from current location to calculate the offset
#         1: from the start of the file to calculate offset
#         2: from the end of the file to calculate the offset
# if u need to open a binary file, should open with ``rb``
f = open("test.txt", 'r')
# 0L the beginning of the file
# f.tell() to get the current position
f.tell()
# 10L
f.seek(10)
# move 15 words forward from current position
f.seek(15, 1)
# # 0L
f.seek(0, 0)
f.tell()
# end of the file: 39L
f.seek(0, 2)
# -5 fro back: 34L
f.seek(-5, 2)
f.tell()

# use readinto method to dump into a buffer which could be defined as your demand
from array import array
f.seek(0, 2)
num = f.tell()
f.seek(0)
# use array to create a buffer: buf
# array('c', '# test file\n# line 1\n# line 2\n# line 3\n')
buf = array('c', ('0' for _ in xrange(num)))
f.readinto(buf)
f.close()

# how to set file IO buffer
# usually, a block is 4096 bytes, only 4096 bytes have been written to buffer, then the buffer will dump to a file
# open("test", "rw+", buffering=) to set buffer
# buffering = 1, line buffer, write a character of '\n' will immediately dump to file
# buffering > 1, full buffer, only write certain bytes could dump to file
# buffering = 0, no buffer, dump to file whatever you input
# buffering default is -1, which represents 4096 bytes(one block)



