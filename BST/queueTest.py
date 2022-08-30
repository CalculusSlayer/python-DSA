# queueTest.py
# Test for queue data structure

import QueueLinkedList as q

def main():
    q1 = q.Queue()
    for i in range(5):
        q1.enqueue(i)
    if q1.isEmpty():
        print("q1 is empty")
    else:
        print("q1 is not empty")
    print(q1)

if __name__ == "__main__":
    main()