## Chapter 15 : Context Managers and else Blocks
Two generally ommited features:
- The `with` statement and context Managers
- The `else` clause in `for`, `while`, and `try` statement

`for`:
The `else` block will run only if and when the `for` loop runs to completion.

`while` :
The `else` block will run only if and when the while loop exits because the condition become falsy.

`try`:
The `else` block will only run if no exception is raised in the `try` block.

    for item in my_list:
        if item.flavor == "banana":
            break
    else:
        raise ValueError("No banana")

### 1. Context Managers
> Context manager objects exist to control a `with` statement, just like iterators exist to control a `for` statement

Context manager protocols:
- `__enter__`
- `__exit__`

The context manager object is the result of evaluating the expression after with, but the value bound to the target variable(in as) is the result of calling `__enter__` on the context manager.

    with open('mirror.py') as fp:
        src = fp.read(60)
Study examples in `mirror.py`
`__exit__` have three arguments:
- `exc_type` : The exception class
- `exc_value` : parameters passed to exception constructor
- `traceback`

### 2. `contextlib` library
`@contextmanager` decorator use `yield` to split the body of function into two parts: before `yield`, code will be executed when interpreter calls `__enter__`; the code after `yield` will run `__exit__` at the end of block.
You can find example code in `List15.5.py`.
The `__enter__` method:
- Invokes the generator function and holds on to the generator object -- `gen`
- Calls `next(gen)` to make it run to the `yield` keyword
- Returns the value yielded by `next(gen)`, so it can be bound to a target variable in the `with/as` form

When the `with` block terminates, the `__exit__` method:
- 
