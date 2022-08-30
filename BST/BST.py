import QueueLinkedList as q 

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    
    def __str__(self):
        x = ""
        def recur(node, n=0):
            nonlocal x
            if node:
                recur(node.rightChild, n+1)
                s1 = str(node.data).ljust(6)
                x += n * " " * 6 + s1 + "\n" * 2
                recur(node.leftChild, n+1)

        recur(self)
        return x   


def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if not rootNode.leftChild:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if not rootNode.rightChild:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)

def main():
    newBST = BSTNode(None)
    insertNode(newBST, 8)
    insertNode(newBST, 16)
    insertNode(newBST, 5)
    insertNode(newBST, 99)
    insertNode(newBST, 11)
    insertNode(newBST, 1)
    insertNode(newBST, 30)

    print(newBST)


if __name__ == "__main__":
    main()
