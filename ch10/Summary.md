## Chapter 10 Sequence Hacking, Hashing, and Slicing
The book said "The best practice for a sequence constructor is to take the data as an interable argument in the constructor."
In python, you don't need to inherit from any special class to create a fully functional class. You just need to implement the method that fulfill the sequence protocol. In the context of object-oriented programming, a protocol is an informal interface defined only in documentation and not in code.

    ## sliceable sequence
    def __len__(self):
        return len(self._components)
    def __getitme__(self, index):
        return self._components[index]
But this implementation can have problems, `vector[1:4]` will return a arrary, rather than another vector object.

     ## A slice aware __getitem
     def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(slef._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            raise TypeError
