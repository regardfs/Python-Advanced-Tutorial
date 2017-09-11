import unicodedata
import string

def shave_marks(txt):
    norm_txt = unicodedata.normalize('NFC', txt)
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)

