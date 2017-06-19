#coding=utf-8
"""
@From book Fluent Python
"""
class DoubleDict(dict):
    kk = {}
    def __setitem__(self, key, value):
        ## In Python 2.7
        super(DoubleDict, self).__setitem__( key, [value] * 2)

def main():
    dd = DoubleDict(one = 1)
    print dd
    dd['two']= 2
    print dd
    dd.update(three = 3)
    print dd


if __name__ == "__main__":
    main()
"""
Result
$ python Test1.py
{'one': 1}
{'two': [2, 2], 'one': 1}
{'three': 3, 'two': [2, 2], 'one': 1}
"""
