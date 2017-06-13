## 1. Brief Introduction
I've been using python for half a year. Since I already have experience in writing C++, python seems not difficult for me. I used this language mostly for processing financial data, but it also restrained my understanding of the language (processing financial data relies heavily on one package : **pandas**). Later on, I begined to learn OOP system in python and find it quite different from static typed language like C++. When reviewing the work, I always think these materials are not pythonic enough.
I've got used to basic python data structure, like list, dict, tuple, set, etc. But when I read other people's code, they import different packages like **collections**, **itertools**. I began to realize, there is also a "STL" in python, but reading those code from [python.org](https://www.python.org/) is tedious and made me fall asleep. One of my friends recommended [Fluent Python](https://www.amazon.cn/s/ref=nb_sb_noss/462-5584630-9055351?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&url=search-alias%3Dstripbooks&field-keywords=fluent+python) to me, and I got really exited about its material.
This project is made to my python playground. It will cover the knowledge taught in the book, combined with my understanding with python doc.

## 2. First class object
Ch5 focus on properties in function. Functions can be categorized as "first-class object".
> **First class object**:
- Created at runtime
- Assigned to a variable or element in a data structure
- Passed as an argument to a Functions
- Returned as the result of a Functions

Functions in C++ are hard to call themselves "first class objects".Python makes "TYPE" between different data structure obscure, and maybe that is the chrisma of this language.
Python2.7 has many higher-order functions, whose parameters are also functions, like `map`, `reduce`, `apply`. But most of the method has been substitued by **list comprehension**.

    list(map(fact, range(6)))
    [fact(n) for n in range(6)]
Higher-order functions can be found in `Lib/functools.py`, or `import functools`
Some may be useful in our code:
- `functools.total_ordering(cls)`
- `functools.reduce`
- `functools.partial`
- `functools.wraps`

`functools.partial` is an interesting tool(works like binding functions in C++).

    from functools import partial
    basetwo = partial(int, base = 2)
    basetwo('10010')
`all(iterable)`: Returns True if every element of the iterable is truthy.
`any(iterable)`: Returns True if any element of the iterable if truthy.

`functools` can mainly be used in **callable objects**. The book summarize 7 possible flavors in python.
- User-defined functions
- Build-in functions
- Methods(class)
- Classes(`__new__`)
- Class instances(`__call__`)
- Generator functions

## 3. Function Introspection
`5.10.py` has marvelous coding style, but my working environment python 2.7 cannot run that. It manifest the power of `*` and `**` to explode iterables and mapping into separate arguments.
`my_tag = {'name':'img', 'title':'Sunset', 'cls':'framed'}`
`tag(**my_tag)`
Here comes a tricky part: Prefixing the my_tag dict with `**` passes all its items as separate arguments, which are then bound to the named parameters.
>Within a function object, the __defaults__ attribute holds a tuple with the default values of positional and keyword arguments. The defaults for keyword-only arguments appear in __kwdefaults__. The names of the arguments, however, are found within the __code__ attribute.

You can test my code in `introspect.py` and `testintrospect.py`.
**Python3 support function programming better**. `5.18.py` can be only useful in Python3.X.

## 4. Functional Programming packages
`5.23.py` introdeces a very useful technique. `cc_name = itemgetter(1,0)`. `operator.attrgetter()` combined with `collections.namedtuple` is also a powerful skill.
I will upload some other [resources](https://docs.python.org/3/howto/functional.html) related to function programming in Python. By definition,
> Functional programming decomposes a problem into a set of functions. Ideally, functions only take inputs and produce outputs, and don't have any internal state that affects the output produced for a given input.

**Functional style discourages functions with side effect that modify internal state or make other changes that aren't visible in the function's return value.** --> **purely function**
There are theoretical and practical advantages to the functional style:
- Formal provability
- Modularity
- Composability
- Ease of debugging and testing

### Iterator
Iterator represent a stream of data; it returns the data one element at a time. Iterators can be materilized by list comprehension.
Generator expressions:
`(expression for expr in sequence1
              if condition1
             for expr2 in sequence2
              if condition2...)`
Generator expressions always have to be written inside parentheses. Note the sequence do not have to be the same length, because they iterated over left to right, not parallel.

### Generators
Generators are a special class of functions that simplify the task of writing iterators. Generators can be thought of as **resumabe function**--> local vairable won't die.

    def generate_ints(N):
      for i in range(N):
        yield i
Values can be sent into generators by calling its `send(value)` method. Generators also become **coroutines**, a more generalized form of subroutines. Coroutines can be entered, exited, and resumed at many different points.

### itertools
- `itertools.starmap(func, iter)`---iter as arguments
- `itertools.filterfalse(predicate, iter)`---return predicate filter false
- `itertools.takewhile(predicate, iter)`---false, end
- `itertools.dropwhile(predicate, iter)`---discard True
- `itertools.combinations(iter, r)`
- `itertools.permutations(iter, r)`
- **`itertool.groupby(iter, key = None)`**
