class DynamicArray:
    
    # testing done
    def __init__(self, capacity: int):
        print(f"Creating a dynamic array ", end="")
        print(f"with a capacity of {capacity}")
        self.capacity = capacity
        self.vals = []
        self.length = 0

    # testing done
    def __repr__(self):
        return repr(self.vals)

    # testing done
    def get(self, i: int) -> int:
        return self.vals[i]

    # testing done
    def insert(self, i: int, n: int) -> None:
        self.vals[i] = n
    
    # testing done
    def pushback(self, n: int) -> None:
        if self.getSize() >= self.getCapacity():
            self.resize()
        self.vals.append(n)
        self.length += 1

    # testing done
    def popback(self) -> int:
        popped_value = self.vals.pop(-1)
        self.length -= 1
        return popped_value

    # testing done
    def resize(self) -> None:
        self.capacity *= 2

    # testing done
    def getSize(self) -> int:
        return self.length   
    
    # testing done
    def getCapacity(self) -> int:
        return self.capacity
