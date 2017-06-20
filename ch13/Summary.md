## Ch13 Operating Overloading: Doing it Right

### Unary Operators
- -(__neg__) : Arithmetic unary negation
- +(__pos__) : Arithmetic unary plus
- ~(__invert__) : Bitwise inverse of integer

### Overloading + for Vector Addition

    def __add__(self, other):
        pairs = itertools.zip_longest(self, other, fillvalue = 0.0)
        return Vector(a + b for a, b in pairs)
`itertools.zip_longest` makes an iterator that aggregates elements from each of the iterables. If the iterables are of uneven length, missing values are filled in with `fillvalue`

    def __radd__(self, other):
        return self + other
`Vector([1,2,3]) + [1,2,3]` will be okay, but the reverse will raise an error. `__radd__` method make the **right add** possible.

### Overloading * for Scalar Multiplication

    def __mul__(self, scalar):
        return Vector(n * scalar for n in self)
    def __rmul__(self, scalar):
        return self * scalar
