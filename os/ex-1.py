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

