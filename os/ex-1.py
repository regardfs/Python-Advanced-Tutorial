# list files end with .sh or .py
# endswith((".sh", ".py"))
# startswith((".sh", ".py"))
# r'' original character
# u'' unicode character


import os
os.listdir(".")
l = os.listdir(".")
[x for x in l if x.endswith(('h','s'))]
[x for x in l if x.startswith(('h','s'))]

# we could get file/dir detail atime/mtime/ctimem, mode, size by os.path
# python2 document: https://docs.python.org/2/library/os.path.html
# python3 document: https://docs.python.org/3/library/os.path.html

os.path.isdir('/root')
os.path.isfile('/etc/passwd')
os.path.islink('/usr/lib64/libsecure.so')

os.path.getatime('test.txt')
os.path.getctime('test.txt')
os.path.getmtime('test.txt')

os.path.getsize('test.txt')
