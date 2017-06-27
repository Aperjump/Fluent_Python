## Chapter 16 : Coroutines
A coroutine is syntatically like a generator: just a function with the `yield` keyword in its body.  The coroutine may receive data from the caller, which uses `.send(datum)` instead of `next()` to feed the coroutine.
> Coroutine : A procedure that collaborates with the caller, yielding and receiving values from the caller.

`send()` method returns the next value yielded by generator iterator or rasie `StopIteration` if generator exits normally. If the generator raises an uncaught exception, it is propogated to `send()` caller.

### Basic Coroutine behavior
See exmaples in `Example16.1.py`, `yield` is used as an expression ()
