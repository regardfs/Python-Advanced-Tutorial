from operator import methodcaller

s = "xyz456123xyz"

methodcaller("find", "xyz", 6)(s)


