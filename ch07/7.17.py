#coding=utf-8
"""
@From book Fluent Python
"""
import time
import functools

def clock(func):
    @functools.wraps(func)
    """
    functools.wraps here is used to transform __name__ and __doc__ of the
    decorated functions
    """
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_list = []
        if args:
            arg_list.append(','.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k,w) for k, w in sorted(kwargs.items())]
            arg_list.append(','.join(pairs))
        arg_str = ','.join(arg_list)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked
@clock
def haha():
    i = 0
    for i in range(10000):
        i+=1
def main():
    haha()

if __name__ == "__main__":
    main()
