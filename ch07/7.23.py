#coding=utf-8
"""
@From book Fluent Python
"""
registry = set()
def register(active = True):
    def decorate(func):
        print('Running register(active=%s)->decorate(%s)'
            %(active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)

        return func
    return decorate

@register(active=False)
def f1():
    print("hahaha")
@register()
def f2():
    print("hohoho")
