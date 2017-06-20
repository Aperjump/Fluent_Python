from Sentence import *

s = Sentence('"The time has come," the Walus said,')
print s
for word in s:
    print(word)

"""
$ python TestingSentence.py
Sentence('"The time ha...e Walus said,')
The
time
has
come
the
Walus
said
"""
