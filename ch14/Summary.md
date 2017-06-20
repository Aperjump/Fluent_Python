## Chapter 14 : Iterables, Iterators, and Generators
> Every colletion in Python is **iterable**, and iterators are used internally to support
- for loops
- Collection types construction and extension
- Looping over text files line by line
- List, dict, and set comprehensions
- Tuple unpacking
- Unpacking actual parameters with * in function calls

The example in `Sentence.py` did not implement `__iter__` method, but can be called through iteration.
The `iter` built-in function:
>
- Checks whether the object implements `__iter__`, and calls that to obtain an iterator.
- If `__iter__` is not implemented, but `__getitem__` is implemented, Python creates an iterator that attempts to fetch items in order, starting from index 0
- If that fails, Python raises `TypeError`, usually saying `C object is not iterable`, where C is the class of the target object

### 1. Iterables Vs iterators
**iterable**: Any object from which the `iter` built-in function can obtain an iterator. Objects implementing an `__iter__` method returning an **iterator** are iterable.
Look at `compare_iterators.py` for example. `StopIteration` signals that the iterator is exhausted.
The standard interface for an iterator has two methods:
- `__next__`
- `__iter__`
**iterator**: Any object that implements the `__nex__` no-argument method that returns the next item in a sequence or raises `StopItration` when there are no more items. Python iterators also implement the `__iter__` method so they are **iterables** as well.

### 2. Classic iterator
> A common cause of errors in building iterables and iterators is to comfuse the two. To be clear: iterables have an `__iter__` method that instantiates a new iterator every time. Iterators implement a `__next__` method that returns individual items, and an `__iter__` method that returns `self`.

See examples in `sentence_iter.py`. Making `Sentence` an iterator can be a bad idea. The idea of iterator is to support **multiple traversals**, which must be possible to obtain multiple independent iterators from the same iterable object, and each iterator must keep its own internal state.

### 3. A Generator Functions
A Pythonic implementation of the same functionality uses a generator function to replace the `SequenceIterator` class.
Any Python function that has the `yield` keyword in its body is a generator function, which when called, returns a generator object. See `Sentence_gen.py`.
A generator function builds a generator object that wraps the body of the function. When we invoke `next(...)` on the generator object, execution advances to the next `yield` in the function body. Finally, when the function body returns, the enclosing generator object raises `StopIteration`, in accordance with the `Iterator` protocol.

def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end')

for c in gen_AB():
    print('-->', C)
