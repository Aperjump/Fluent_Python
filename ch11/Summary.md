## Chapter 11 Interfaces: From Protocols to ABCs
Protocols are defined as the informal interfaces that make polymorphism work in languages with dynamic typing. Protocols are interfaces. The idea of interface is really simple - it is the description of how an object behaves. An interface tells us what an object can do to play it’s role in a system. In object oriented programming, an interface is a set of publicly accessible methods on an object which can be used by other parts of the program to interact with that object. Interfaces set clear boundaries and help us organize our code better.
For example:

    class book:
        ## implement read method
        def read():
        {
          ...
        }
        ## implement iter
        def __iter__():
        {

        }
This book class have `read` and `__iter__` method, meaning that it can be treated like a file object or iterale object. See? We didn't use book to inherit some other object. By implementing several methods, this class have the behavior of other class. Besides, you can also add attribute during run time.

    >>>def getlength(book):
          return len(book.item)
    >>>book.__len__ = getlength
    >>>len(book)
This is a exmaple of **monkey patching**: changing a class or module at runtime, without touching the source code. Monkey patching is powerful, but the code that does the actual patching is very tightly coupled with program to be patched, often handling private and undocumented part.

### ABCs in Standard Library
Most ABCs are defined in `collections.abc` module.
You can find a ABC exaple in `Tombala.py'. And the best way to declare an ABC is to subclass `abc.ABC`. But this is new in Python 3.4.
In Python 3+, you can write:

    class Tombola(metaclass = abc.ABCMeta):
In Python 2.7:

    class Tombola(object):
        __metaclass__ = abc.ABCMeta
