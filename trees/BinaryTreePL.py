#from typing import Optional

class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size
    
    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        return "The value has been successfully inserted"

    def searchNode(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return "Not found"

    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index], end='->')
        self.preOrderTraversal(2 * index)
        self.preOrderTraversal(2 * index + 1)

    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(2 * index)
        print(self.customList[index], end='->')
        self.inOrderTraversal(2 * index + 1)

    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(2 * index)
        self.postOrderTraversal(2 * index + 1)
        print(self.customList[index], end='->')

    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i], end='->')

    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "No nodes to delete"
        for i in range(1, self.lastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "Node has been successfully deleted"

    def clear(self):
        for i in range(1, self.lastUsedIndex+1):
            self.customList[i] = None
        self.lastUsedIndex = 0


def main():
    newBT = BinaryTree(8)
    print(newBT.insertNode('Drinks'))
    print(newBT.insertNode('Hot'))
    print(newBT.insertNode('Cold'))
    print(newBT.insertNode('Tea'))
    print(newBT.insertNode('Coffee'))

    # print(newBT.searchNode('Hot'))

    newBT.preOrderTraversal(1)
    print()
    print('*' * 40)
    newBT.inOrderTraversal(1)
    print()
    print('*' * 40)
    newBT.postOrderTraversal(1)
    print()
    print('*' * 40)
    newBT.levelOrderTraversal(1)
    print()
    print('*' * 40)

    newBT.deleteNode('Hot')
    newBT.levelOrderTraversal(1)
    print()
    print('*' * 40)

    print("Clearing the BT")
    newBT.clear()
    newBT.levelOrderTraversal(1)
    print()
    print('*' * 40)

    

if __name__ == "__main__":
    main()
