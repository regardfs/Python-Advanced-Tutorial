# decode && encode type should be equal

str1 = u"我在学习python"
# '\xe6\x88\x91\xe5\x9c\xa8\xe5\xad\xa6\xe4\xb9\xa0python'
str1.encode("utf8")
# u"我在学习python"
print str1.encode("utf8").decode("utf8")

# python2 str unicode u"学习", "abc"
# python3 bytes str "学习", b"abc"

# in python3 env
f = open("test.txt", "wt", encoding='urf8')
f.write("呵呵")
f.close()

f = open("test.txt", "rt", encoding='urf8')
f.read()
f.close()