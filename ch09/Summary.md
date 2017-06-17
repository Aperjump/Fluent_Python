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
Their comparison can be found in `classmethod_staticmethod.py`
