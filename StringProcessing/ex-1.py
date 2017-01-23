# re.findall return a list
import re
regex = ur"\[P\] (.+?) \[/P\]+?"
line = "President [P] Barack Obama [/P] met Microsoft founder [P] Bill Gates [/P], yesterday."
person = re.findall(regex, line)
print(person)

# re.match return an object of firstly matched


# re.search search (string[, pos[, endpos]])
pattern = re.compile("a")
# <_sre.SRE_Match at 0x111509cc8>
pattern.search("abcde")
# <_sre.SRE_Match at 0x111509d30>
pattern.search("abcde", 0)
# None
pattern.search("abcde", 1)

# re.sub
p = re.compile( '(one|two|three)')
# 'num word num words num words'
p.sub( 'num', 'one word two words three words')
# 2017-01-21 to 21/01/2017
re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\g<day>/\g<month>/\g<year>', '2017-01-27')



# re.split
# ['test', 'test', 'test', '']
re.split('\W+', 'test, test, test.')
# [' test ', ', ', ' test ', ', ', ' test ', '.', '']
re.split('(\W+)', ' test, test, test.')
# [' test ', ' test, test.']
re.split('\W+', ' test, test, test.', 1)
