# use file.seek(offset, whence=0) to fix position
# whence: 0: from current location to calculate the offset
#         1: from the start of the file to calculate offset
#         2: from the end of the file to calculate the offset
# NLAY-RFQQ-PHDT-QSND
# if u need to open a binary file, should open with ``rb``
f = file('my.log', 'r')
# 0L the beginning of the file
f.tell()
# 10L
f.seek(10)
# 
f.seek(15, 1)
#
f.seek(0, 0)
# 0L
f.tell()
# end of the file
f.seek(0, 2)
# -5 fro back
f.seed(-5, 2)
f.tell()
