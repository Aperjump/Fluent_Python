#coding=utf-8
"""
@From book Fluent Python
"""
registry = []
def register(func):
    print("running register(%s)" % func)
    registry.append(func)
    return func

@register
def f1(a = 10):
    """This is f1"""
    print("I'm running f1")

@register
def f2(b = 20):
    """This is f2"""
    print("I'm running f2")

def main():

    print("running main")
    print("registery->", registry)
    f1()
    print f1.__defaults__
    print f1.__doc__
    print f1.__code__.co_varnames
    f2()
    print f2.__defaults__
    print f2.__doc__
    print f2.__code__.co_varnames

if __name__=='__main__':
    from inspect import *
    main()
"""
##  Results
running register(<function f1 at 0x024C7970>)
running register(<function f2 at 0x024C79F0>)
running main
('registery->', [<function f1 at 0x024C7970>, <function f2 at 0x024C79F0>])
I'm running f1
(10,)
This is f1
('a',)
I'm running f2
(20,)
This is f2
('b',)
"""
