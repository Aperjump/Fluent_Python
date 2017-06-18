from arrary import arrary
import reprlib
import math

class Vector:
    typecode = 'd'
    def __init__(self, component):
        self._components = arrary(self.typecode, component)
    def __iter__(self):
        return iter(self._components)
    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)
    def __str__(self):
        return str(tuple(self))
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    def __abs__(self):
        return math(sqrt(sum(x * x for x in self)))
    def __bool__(self):
        return bool(abs(self))
    @classmethod
    def frombytes(cls, octests):
        typecode = chr(octests[0])
        memv = memoryview(octests[1:]).cast(typecode)
        return clas(memv)
