#coding=utf-8
"""
@From book Fluent Python
"""
from test import clock
@clock
def fibonaci(n):
    if n < 2:
        return n
    return fibonaci(n - 2) + fibonaci(n - 1)

if __name__ == "__main__":
    print fibonaci(10)
"""
$ python 7.18.py
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(3) -> 2
[0.00000000s] fibonaci(4) -> 3
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(3) -> 2
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(3) -> 2
[0.00000000s] fibonaci(4) -> 3
[0.00000000s] fibonaci(5) -> 5
[0.00000000s] fibonaci(6) -> 8
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(3) -> 2
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(3) -> 2
[0.00000000s] fibonaci(4) -> 3
[0.00000000s] fibonaci(5) -> 5
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(3) -> 2
[0.00000000s] fibonaci(4) -> 3
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(3) -> 2
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(3) -> 2
[0.00000000s] fibonaci(4) -> 3
[0.00000000s] fibonaci(5) -> 5
[0.00000000s] fibonaci(6) -> 8
[0.00000000s] fibonaci(7) -> 13
[0.00000000s] fibonaci(8) -> 21
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(3) -> 2
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(3) -> 2
[0.00000000s] fibonaci(4) -> 3
[0.00000000s] fibonaci(5) -> 5
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(3) -> 2
[0.00000000s] fibonaci(4) -> 3
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(3) -> 2
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(3) -> 2
[0.00000000s] fibonaci(4) -> 3
[0.00000000s] fibonaci(5) -> 5
[0.00099993s] fibonaci(6) -> 8
[0.00099993s] fibonaci(7) -> 13
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(3) -> 2
[0.00000000s] fibonaci(4) -> 3
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(3) -> 2
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(3) -> 2
[0.00000000s] fibonaci(4) -> 3
[0.00000000s] fibonaci(5) -> 5
[0.00000000s] fibonaci(6) -> 8
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(3) -> 2
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(3) -> 2
[0.00000000s] fibonaci(4) -> 3
[0.00000000s] fibonaci(5) -> 5
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(3) -> 2
[0.00000000s] fibonaci(4) -> 3
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(3) -> 2
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(0) -> 0
[0.00000000s] fibonaci(1) -> 1
[0.00000000s] fibonaci(2) -> 1
[0.00000000s] fibonaci(3) -> 2
[0.00000000s] fibonaci(4) -> 3
[0.00000000s] fibonaci(5) -> 5
[0.00000000s] fibonaci(6) -> 8
[0.00000000s] fibonaci(7) -> 13
[0.00000000s] fibonaci(8) -> 21
[0.00099993s] fibonaci(9) -> 34
[0.00099993s] fibonaci(10) -> 55
"""
