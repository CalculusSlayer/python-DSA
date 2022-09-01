from CustomHeapq import CustomHeapq

def main():
    h1 = CustomHeapq()
    h1.push(4)
    h1.push(3)
    h1.push(10)
    h1.push(5)
    h1.push(4)
    h1.push(4)
    h1.push(5)

    print(h1)
    while len(h1) > 3:
        print(h1.pop())
    print(h1.peak())

    print(h1)

if __name__ == "__main__":
    main()