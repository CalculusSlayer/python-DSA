# Nayeel Imtiaz
# 8/31/22

# CustomHeapq.py
# - Heap class with custom comparator implemented with
# python's built-in heapq module.
import heapq

class CustomHeapq:
    # initial: Any iterable to initialize heap (preferably a list).
    # key: Custom comparator function to be passed in. This will
    # ensure that the heap maintains the order you want it to.

    # Return value: CustomHeapq object.
    def __init__(self, initial=None, key=lambda x: x):
        self.index = 0
        self.key = key
        if initial:
            self._data = [(key(val), index, val)
                            for index, val in enumerate(initial)]
            heapq.heapify(self._data)
            self.index = len(self._data)
        else:
            self._data = []

    # Return string representation of list containing
    # the values of the heap when print() or str() is called on it.
    # EX: print(h1), str(h1) where h1 is a CustomHeapq object.
    def __str__(self):
        if len(self._data) == 0:
            return "Empty heap"
        return str([t[2] for t in self._data])

    # Return true representation of heap. Use for debugging purposes.
    # EX: repr(h1) where h1 is a CustomHeapq object.
    def __repr__(self):
        return str([t for t in self._data])

    # Return length of the heap object
    # when len() is called on it. Ex: len(h1) where
    # h1 is a CustomHeapq object.
    def __len__(self):
        return len(self._data)
    
    # Push value into heap. Nothing is returned.
    def push(self, val):
        heapq.heappush(self._data, (self.key(val), self.index, val))
        self.index += 1
    
    # Pop smallest value from heap (value is removed) and return it.
    def pop(self):
        return heapq.heappop(self._data)[2]
    
    # Return the smallest value in the heap (value is NOT removed).
    def peak(self):
        return self._data[0][2]
