## Chapter 7 Function Decorators and Closures
This chapter highlight closures' importance in decorators and asynchronous programming.
> A decorator is a callable that takes another function as argument. The decorator may perform some processing with the decorated function, and returns it or replaces it with another function or callable object.
`target = decorate(target)`

Two important features for **decorators**
- Decorators have to power to replace the decorated function with a different one
- Decorators are executed immediately when a module is loaded

Most decorators change the decorated function. They usually do it by defining an inner function and return it to replace the decorated function. **Code that uses inner functions almost always depends on closures to operate correctly**.

Closures:
> A closure is a function with an extended scope that encompasses nonglobal variables referenced in the body of the function but not defined there.

You can test code in `7.11.py`. The binding for series is kept in the `__closure__` attribute of the returned function.
A closure is a function that retains the bindings of the free variables that exist when the function is defined, so that they can be used later when the function is invoked and the defining scope is no longer available.
`nonloccal` lets you flag a variable as a free variable even when it is assigned a new value within the function.

## Decorators in Standard Library
Three built-in functions: `property`, `classmethod`, `staticmethod`.
In SL : `lru_cache`, `singledispatch`
### `lru_cache`
`functools.lru_cache` implements memorization: an optimization technique that works by saving the results of previous invocations of an expensive function. See examples in `7.19.py`.
`functool.lru_cache(maxsize = 128, typed = False)` maxsize should be a power of 2. `lru_cache` use a dict to store the results, and the keys are made from the positional and keyword arguments used in the calls.
`function.cache_info()` will return a named_tuple showing current state.

### `singledispatch`
If you decorate a plain function with `@singledispatch`, it becomes a `generic function` : a group of functions to perform the same operation in different ways.

    from functools import singledispatch
    @singledispatch
    def htmlize(obj):
      content = html.esape(repr(obj))
      return '<pre>{}</pre>'.format(content)
    @htmlize.register(str)
    def _(text):
      content = html.escape(text).replace('\n','<br>\n')

For each additional type to receive special treatment, register a new function.
> A notable quality of the `singledispatch` mechanism is that you can register sepcialized functions anywhere in the system, in any module. If you later add a module with a new user-defined type, you can easily provide a new custom function to handle the type.

## Parameterized Decorators
**make a decorator factory that take arguments and return a decorator**
