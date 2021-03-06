#coding=utf-8
"""
@From book Fluent Python
"""
from array import arrary
import math

class Vector2d:
    typecode = 'd'
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    ## __iter__ makes the class unpackable
    ## x, y = vector
    def __iter__(self):
        return (i for i in (self.x, self.y))
    ## {!r} to get their repr
    ## *self, feed x and y component to format
    def __repr__(self):
        class_name = type(self)._name
        return `{}({!r}, {!r})`.format(class_name, *self)
    def __str__(self):
        return str(tuple(self))
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    def __abs__(self):
        return math.hypot(self.x, self.y)
    def __bool__(self):
        return bool(abs(self))
