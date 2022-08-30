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
    
    #print(newBST)


if __name__ == "__main__":
    main()