## Chapter 9 A Pythonic Object

### Object Representation
- `repr()` : Return a string representing the object as the developer wants to see it->`__repr__`
- `str()` : Return a string representing the object as the user wants to see it -> `__str__`
- `bytes()` : byte sequence -> `__bytes__`
-  `format()` : use special formatting codes ->`__format__`


    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)
`@classmethod` define a method that operates on the class and not on instances. In contrast, `@staticmethod` decorater changes a method so that it receives no special first argument.
Their comparison can be found in `classmethod_staticmethod.py`.

#### Format displays
`format(my_obj, format_spec)`
`'1 BRL = {rate:0.2f} USD'.format(rate = brl)`
`1 BRL = 0.41 USD`
Note `{0.mass:5.3e}`, the left part is the field_name part of the replacement field syntax,; the right part is the formatting specifier.

A customized format:

    def __format__(self, fmt_spec = ''):
      components = (format(c, fmt_spec) for c in self)
      return '({} ,{})'.format(*components)

#### Hashable


    def __hash__(self):
      return hash(self.x) ^ hash(self.y)
In python, there is no **private** variables.What we have is name mangling. If you name an instance attribute in the form `__mood`, Python stores the name in the instance `__dict__` prefixed with a leading underscore and the class name.
meanning that `__mood`-->`_Dog__mood`
The single undersocre prefix has no special meaning to python interpreter when used in attribute names, but it's a very strong convention among Python programmers that you should not access such attributes from outside the class.

#### __slots__
Python normally stores attribute in `__dict__`, but this behavior have high perfomance cost. `__slots__` stores attributes in tuple, and can help you save a lot of memory.

    class Vector2d:
      __slots__ = ('_x','_y')
      typecode = 'd'
