import QueueLinkedList as queue # not used yet

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

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data, end=" > ")
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    preOrderTraversal(rootNode.leftChild)
    print(rootNode.data, end=" > ")
    preOrderTraversal(rootNode.rightChild)


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
    print(rootNode.data, end=" > ")


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue() # root is a regular Node type
            print(root.value.data, end=" > ")
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

def searchNode(rootNode, newValue):
    if rootNode.data == newValue:
        return f"The value {newValue} was found"
    elif newValue < rootNode.data:
        if rootNode.leftChild is not None:
            return searchNode(rootNode.leftChild, newValue)
        else:
            return f"The value {newValue} was NOT found"
    else:
        if rootNode.rightChild is not None:
            return searchNode(rootNode.rightChild, newValue)
        else:
            return f"The value {newValue} was NOT found"

def minValueNode(bstNode):
    current = bstNode
    while current.leftChild is not None:
        current = current.leftChild 
    return current 

def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode 
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None     # optional b/c rootNode is replaced by temp when returned
            return temp
        
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None     # optional b/c rootNode is replaced by temp when returned
            return temp 
        
        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode

def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    print("Successfully cleared BST")



