#coding=utf-8
"""
@From book Fluent Python
Only available on Python 3.X
"""
import inspect
sig = inspect.signature(tag)
my_tag = {'name':'img','title':'Sunset',
          'src':'sunset.jpg','cls':'framed'}
bound_args = sig.bind(**my_tag)
for name, value in bound_args.arguments.items():
    print(name, "=", value)

del my_tag['name']
bound_args = sig.bind(**my_tag)
