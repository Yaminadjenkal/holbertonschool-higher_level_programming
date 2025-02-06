#!/usr/bin/python3
"""class that defined a
countediterator
"""


class CountedIterator:
    def __init__(self, iterable):
        """initialization of itaration method
        """
        self.iterable = iterable
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """initialization of the iteration methode
        """
        return self

    def __next__(self):
        """defined the methode to next to the element """
        try:
            item = next(self.iterator)
            self.count += 1
            print(f"Iteration {self.count}: {item}")
            return item
        except StopIteration:
            raise StopIteration
