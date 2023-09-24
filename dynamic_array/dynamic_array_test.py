import dynamic_array as d

def main():
    print("*" * 5 + " TESTING INIT " + "*" * 5)
    da1 = d.DynamicArray(5)
    # print(dir(da1))
    print(da1)
    print(f"Capacity of da1: {da1.getCapacity()}")
    print(f"Length of da1: {da1.getSize()}")
    print()

    print("*" * 5 + " TESTING PUSHBACK " + "*" * 5)
    for i in range(1, 6):
        print(f"Push {i * 10}")
        da1.pushback(i * 10)    
    print(da1)
    print(f"Capacity of da1: {da1.getCapacity()}")
    print(f"Length of da1: {da1.getSize()}")
    print()

    print("*" * 5 + " TESTING GET " + "*" * 5)
    for i in range(da1.getSize()):
        print(f"da1[{i}] = {da1.get(i)}")  
    print(da1)
    print(f"Length of da1: {da1.getSize()}")
    print()

    print("*" * 5 + " TESTING PUSHBACK > CAPACITY " + "*" * 5)
    for i in range(6, 9):
        print(f"Push {i * 10}")
        da1.pushback(i * 10)
    print(da1)
    print(f"Capacity of da1: {da1.getCapacity()}")
    print(f"Length of da1: {da1.getSize()}")
    print()

    print("*" * 5 + " TESTING POPBACK " + "*" * 5)
    for i in range(3):
        print(f"Pop {da1.vals[-1]}")
        da1.popback()
    print(da1)
    print(f"Length of da1: {da1.getSize()}")
    print()

    print("*" * 5 + " TESTING INSERT " + "*" * 5)
    x = 42
    for i in range(da1.getSize()):
        print(f"Change da1[{i}] = {da1.get(i)} to ", end="")
        print(f"da1[{i}] = {x}")
        da1.insert(n=x, i=i)
    print(da1)
    print(f"Length of da1: {da1.getSize()}")
    print()


if __name__ == '__main__':
    main()