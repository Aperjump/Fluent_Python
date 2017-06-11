"""
author : Aperjump
email : wangwei_aperion@163.com
"""
from introspect import *
"""
from inspect import signature
## Seems to available only in 3.X
"""
print func.__defaults__
print func.__code__.co_varnames
print func.__code__.co_argcount

"""sig = signature(func)
str(sig)
for name, para in sig.parameters.items():
    print(par.kind, " : ", name, " = ", para.default)
"""
