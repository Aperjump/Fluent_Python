## Chapter 16 : Coroutines
A coroutine is syntatically like a generator: just a function with the `yield` keyword in its body.  The coroutine may receive data from the caller, which uses `.send(datum)` instead of `next()` to feed the coroutine.
> Coroutine : A procedure that collaborates with the caller, yielding and receiving values from the caller.
