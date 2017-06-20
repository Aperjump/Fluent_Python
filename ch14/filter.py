"""
Only valid in Python3.X
"""
from itertools import *
def vowel(c):
    return c.lower() in 'aeiou'

list(filter(vowel, 'Aardvark'))
list(filterfalse(vowel, 'Aardvark'))
list(dropwhile(vowel, 'Aardvark'))
list(takewhile(vowel, 'Aardvark'))
list(compress('Aardvark', (1,0,1,1,0,1)))
list(islice('Aardvark', 4))
list(islice('Aardvark', 4, 7))
