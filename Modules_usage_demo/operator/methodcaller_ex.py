from operator import methodcaller

s = 'The time has come'
upcase = methodcaller('upper')
upcase(s)
hiphenate = methodcaller('replace', ' ', '-')
hiphenate(s)


