## Ch12 Inheritance: For Good or For Worse
This chapter talks about two main issues:
- The pitfalls of subclassing from built-in types
- Multiple inheritance and the method resolution order

When subclassing built-in types, an overriding member function may not be used by other functions. The problem can be illustrated by `Test1.py`. Subclassing built-in types like `dict` or `list` or `str` directly is error-prone because the built-in methods mostly ignore user-defined overrides. Instead of subclassing the built-ins, derive your classes from the `collections` using `UserDict`, `UserList`, and `UserString`, which are designed to be easily extended(not available for Python 2.7). The problem only occurs to method delegation within C language implementation of the built-in types.

### Multiple Inheritance and Method Resolution order
