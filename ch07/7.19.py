#coding=utf-8
"""
@From book Fluent Python
"""
import functools
from test import clock
"""
We cannot make notation under a decorator
lru_cache must be invoked with `()`
"""
@functools.lru_cache()
@clock
def fibonaci(n):
    if n < 2:
        return n
    return fibonaci(n - 2) + fibonaci(n - 1)

if __name__ == "__main__":
    print(fibonaci(10))
    """
    fibonaci.cache_info() will return a named_tuple
    """
    print(dir(fibonaci))

"""
In Python 2.7:
$ python 7.19.py
Traceback (most recent call last):
  File "7.19.py", line 11, in <module>
    @functools.lru_cache()
AttributeError: 'module' object has no attribute 'lru_cache'

In Python 3.6:
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.06400347s] fibonaci(2) -> 1
[0.00000000s] fibonaci(3) -> 2
[0.06700373s] fibonaci(4) -> 3
[0.00000000s] fibonaci(5) -> 5
[0.06900382s] fibonaci(6) -> 8
[0.00000000s] fibonaci(7) -> 13
[0.07300425s] fibonaci(8) -> 21
[0.00000000s] fibonaci(9) -> 34
[0.07300425s] fibonaci(10) -> 55
55
"""
