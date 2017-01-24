# use re module to process string

# re.findall return a list
import re
regex = ur"\[P\] (.+?) \[/P\]+?"
line = "President [P] Barack Obama [/P] met Microsoft founder [P] Bill Gates [/P], yesterday."
person = re.findall(regex, line)
print(person)

# re.match return an object of firstly matched

# re.search: search (string[, pos[, endpos]]) search string with start and end position
pattern = re.compile("a")
# <_sre.SRE_Match at 0x111509cc8>
pattern.search("abcde")
# <_sre.SRE_Match at 0x111509d30>
pattern.search("abcde", 0)
# None
pattern.search("abcde", 1)

# re.sub: substitute with given string
p = re.compile('(one|two|three)')
# 'num word num words num words'
p.sub('num', 'one word two words three words')
# 2017-01-21 to 21/01/2017
re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\g<day>/\g<month>/\g<year>', '2017-01-27')

s = "\rqwe\rshakdhsak\r\t"
# or p = re.compile('(\r|\t)'); p.sub("", s)
re.sub("[\r\t]", "", s)

# re.split: split given string with pattern
# ['test', 'test', 'test', '']
re.split('\W+', 'test, test, test.')
# [' test ', ', ', ' test ', ', ', ' test ', '.', '']
re.split('(\W+)', ' test, test, test.')
# [' test ', ' test, test.']
re.split('\W+', ' test, test, test.', 1)

# remove character that we do not need in string
# 1.translate: str.translate and unicode.translate
# str.translate: S.translate(table [,deletechars]) -> string

import string
# build string translate table which will translate strings as you set when run translate method with argument of
# string table
s = "qazwsxpl,okm"
# string.maketrans("qazpl,", "pl,qaz") and you may print to observe what has been changed
s.translate(string.maketrans("qazpl,", "pl,qaz"))

# remove ``qaz,``
s.translate(None, 'qaz,')

# unicode.translate
unis = u"pīn yīn"
# u'p\u012bn y\u012bn'
unis
# u'pin yin'
unis.translate({0x012b: u'i'})

# 2.use replace, but just one character that you could replace
str2_1 = "_hello,world"
str2_1.replace("_", "")
str2_1.replace(",", ":")

# 3.remove space/tab in the start/end position in strings
#   strip, be default, it strip space character: " ", but you could set characters as you like
str3_1 = "    hello, world    "
str3_1.strip()
str3_1.lstrip()
str3_1.rstrip()
str3_1.strip('hd')
str3_2 = "hello, world"
# would echo ``ello, worl``
str3_2.strip("hd")
