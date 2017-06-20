"""
Only valid in Python3.X
"""
from itertools import *

sample = [5,4,2,8,7,6,3,0,9,1]
list(accumulate(sample))
list(accumulate(sample, min))
list(accumulate(sample, max))
