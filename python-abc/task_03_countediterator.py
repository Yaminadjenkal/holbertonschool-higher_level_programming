#!/usr/bin/python3
class CountedIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self.iterator)
            self.count += 1
            print(f"Iteration {self.count}: {item}")
            return item
        except StopIteration:
            raise StopIteration
