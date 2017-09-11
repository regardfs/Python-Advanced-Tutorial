from unicodedata import normalize, name
# normalize('NFC', user_text)
ohm = '\u2126'
name(ohm)
ohm_c = normalize('NFC', ohm)
name(ohm_c)
normalize('NFC', ohm) == normalize('NFC', ohm_c) # True
