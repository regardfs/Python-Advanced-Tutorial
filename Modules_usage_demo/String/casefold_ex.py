from unicodedata import normalize

s1  = 'cafe\u0301'
s2 = 'café'
s3 = 'Cafe\u0301'
s4 = 'CAfé'

normalize('NFC', s1) == normalize('NFC', s2)

normalize('NFC', s1) == normalize('NFC', s3.casefold())

normalize('NFC', s4.casefold() ) == normalize('NFC', s2)