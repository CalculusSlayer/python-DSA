import BinaryHeap as bh 

def main():
    newHeap = bh.Heap(5)
    bh.insertNode(newHeap, 100, "Max")
    bh.insertNode(newHeap, 200, "Max")
    bh.insertNode(newHeap, 300, "Max")


    # bh.insertNode(newHeap, 20, "Max")
    # bh.insertNode(newHeap, 1, "Max")
    # bh.insertNode(newHeap, 200, "Max")
    bh.levelOrderTraversal(newHeap)
    #print(bh.extractNode(newHeap, "Max"))
    #bh.levelOrderTraversal(newHeap)

if __name__ == "__main__":
    main()