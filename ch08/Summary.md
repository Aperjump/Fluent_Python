## Chapter 8 Object References, Mutability, and Recycling
In python, create object at the right hind side, and then the variable on the left is bound to the object.
identity comparison and equality:

    A = {'a':1,'b':2}
    B = A
    """
    >>> A is B
    True
    >>> A == B
    True
Example of aliasing, where `__eq__` compares their values
`==`  operator compares the values of objects, while `is` compares their identity. For singleton:
`x is None` or `x is not None` is more appropriate.
The `copy` module provides `deepcopy` and `copy` functions that return deepcopy and shallowcopy of any objects.
Since python functio pass parameter by copying each parameters' reference inside, it's not a good idea to pass mutable objects.

    class Bus:
      def __init__(self, passengers = None):
        if passengers is None:
          self.passengers = []
        else:
          self.passengers = list(passengers)
      def pick(self, name):
        self.passengers.append(name)
      def drop(self, name):
        self.passengers.remove(name)

### del and garbage collection
> The `del` statement deletes names, not objects -> `<shared_ptr>` in C++
The `__del__` method do not cause the disposal of instance, and should only be called by ingterpreter. 
