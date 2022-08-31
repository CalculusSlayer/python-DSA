import BST

def main():
    newBST = BST.BSTNode(None)
    BST.insertNode(newBST, 8)
    BST.insertNode(newBST, 16)
    BST.insertNode(newBST, 5)
    BST.insertNode(newBST, 99)
    BST.insertNode(newBST, 11)
    BST.insertNode(newBST, 1)
    BST.insertNode(newBST, 30)

    BST.preOrderTraversal(newBST)
    print()
    BST.inOrderTraversal(newBST)
    print()
    BST.postOrderTraversal(newBST)
    print()
    BST.levelOrderTraversal(newBST)
    print()

    print(BST.searchNode(newBST, 8))
    print(BST.searchNode(newBST, 69))
    print(BST.searchNode(newBST, 16))
    print(BST.searchNode(newBST, 1))

    
    print(newBST)
    print()
    #BST.deleteNode(newBST, 8)
    #BST.deleteNode(newBST, 1)
    BST.deleteNode(newBST, 5)
    BST.deleteNode(newBST, 8)
    print(newBST)
    print()
    # print("delete 1000?")
    # BST.deleteNode(newBST, 1000)
    # print(newBST)
    # print("result?")
    BST.deleteNode(newBST, 11)
    print()



    #BST.levelOrderTraversal(newBST)
    print(newBST)
    
    BST.deleteBST(newBST)
    print(newBST)


if __name__ == "__main__":
    main()