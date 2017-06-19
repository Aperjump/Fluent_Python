## Ch12 Inheritance: For Good or For Worse
This chapter talks about two main issues:
- The pitfalls of subclassing from built-in types
- Multiple inheritance and the method resolution order

When subclassing built-in types, an overriding member function may not be used by other functions. The problem can be illustrated by `Test1.py`. Subclassing built-in types like `dict` or `list` or `str` directly is error-prone because the built-in methods mostly ignore user-defined overrides. Instead of subclassing the built-ins, derive your classes from the `collections` using `UserDict`, `UserList`, and `UserString`, which are designed to be easily extended(not available for Python 2.7). The problem only occurs to method delegation within C language implementation of the built-in types.

### Multiple Inheritance and Method Resolution order
Learn `diamond_problem.py`. The ambiguity of a call like `d.pong()` is resolved because Python follows a specific order when traversing the inheritance graph. That order is called **MRO**: method resolution order. Classes have an attribute called `__mro__` holding a tuple or refereces to the superclasses in MRO order(not in python 2.7). Bypass the MRO and invoke a method on a superclass directly: `A.ping(self)`.

### Multiple Inheritance Advice form the book
1. Distinguish Interface Inheritance from implementation Inheritance
2. Make Interfaces Explicit with ABCs
3. Use Mixins for Code Reuse
A mixins merely bundles methods for reuse.
4. Make Mixins Explicit by Naming
5. An ABC may also be a Mixin, The reverse is not true
A mixin should never be subclassed alone except by another.
6. Don't Subclass from More Than One Concrete Class
7. Provide Aggregate Classes to UserString
8. Favor Object Composition Over Class Inheritance
