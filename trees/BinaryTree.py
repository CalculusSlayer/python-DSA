from typing import Optional, Union
import sys

class TreeNode:
    
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(f"-> {rootNode.data} ", end="")
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(f"-> {rootNode.data} ", end="")
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(f"-> {rootNode.data} ", end="")

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        queue = []
        queue.append(rootNode)
        while len(queue) != 0:
            root = queue.pop(0)
            print(f"-> {root.data} ", end="")
            if root.leftChild is not None:
                queue.append(root.leftChild)

            if root.rightChild is not None:
                queue.append(root.rightChild)


def searchBT(rootNode: Optional[TreeNode],
        nodeValue: any) -> str:
    if not rootNode:
        return "The BT is empty"
    else:
        queue = []
        queue.append(rootNode)
        while len(queue) != 0:
            root = queue.pop(0)
            if root.data == nodeValue:
                return "Success"
            if root.leftChild is not None:
                queue.append(root.leftChild)

            if root.rightChild is not None:
                queue.append(root.rightChild)
        return "Not found"

def insertNodeBT(rootNode: Optional[TreeNode], newNode: Optional[TreeNode]) -> Optional[TreeNode]:
    if not rootNode:
        # rootNode = newNode # has no effect
        return newNode
    else:
        queue = []
        queue.append(rootNode)
        while (len(queue) != 0):
            root = queue.pop(0)
            if root.leftChild is not None:
                queue.append(root.leftChild)
            else:
                root.leftChild = newNode
                return rootNode
            
            if root.rightChild is not None:
                queue.append(root.rightChild)
            else:
                root.rightChild = newNode
                return rootNode

def getDeepestNode(rootNode: Optional[TreeNode]) -> Optional[TreeNode]:
    if not rootNode:
        return
    else:
        queue = []
        queue.append(rootNode)
        while (len(queue) != 0):
            root = queue.pop(0)
            if root.leftChild is not None:
                queue.append(root.leftChild)
            if root.rightChild is not None:
                queue.append(root.rightChild)
        deepestNode = root
        return deepestNode

def deleteDeepestNode(
        rootNode: Union[None, TreeNode],
        dNode: Union[None, TreeNode]
        ) -> Union[None, TreeNode]:
    if not rootNode:
        print("BT is empty")
        return None
    else:
        queue = []
        queue.append(rootNode)
        while (len(queue) != 0):
            root = queue.pop(0)
            if root is dNode:
                # root = None # appears to do nothing since
                              # change is made to copy of
                              # the passed in rootNode

                return None # This will make BT empty tho
            if root.rightChild:
                if root.rightChild is dNode:
                    root.rightChild = None
                    return rootNode
                else:
                     queue.append(root.rightChild)
            if root.leftChild:
                if root.leftChild is dNode:
                    root.leftChild = None
                    return rootNode
                else:
                     queue.append(root.leftChild)
    print("failed to delete deepest node")
    return rootNode

def deleteNodeBT(
        rootNode: Optional[TreeNode], 
        nodeValue: any
        ) -> Optional[TreeNode]:
    if not rootNode:
        print("The BT is empty")
        return
    else:
        queue = []
        queue.append(rootNode)
        while (len(queue) != 0):
            root = queue.pop(0)
            if root.data == nodeValue:
                dNode = getDeepestNode(rootNode) # get the deepest node and assign it to dNode
                root.data = dNode.data  # assign dNode data to current tree node data
                print("The node has been successfully deleted")
                return deleteDeepestNode(rootNode, dNode)
            if root.leftChild is not None:
                queue.append(root.leftChild)

            if root.rightChild is not None:
                queue.append(root.rightChild)
        
        print("Could not find node to delete")
        return rootNode

def clearBT(rootNode):
    '''
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BT was successfully deleted."
    '''
    return # None represents an emtpy Binary Tree

def main():
    a = TreeNode(1)
    b = a

    print(hash(a))
    print(hash(b))
    '''
    newBT = TreeNode("Drinks")
    leftChild = TreeNode("Hot")
    tea = TreeNode("Tea")
    coffee = TreeNode("Coffee")
    leftChild.leftChild = tea
    leftChild.rightChild = coffee
    
    rightChild = TreeNode("Cold")
    newBT.leftChild = leftChild
    newBT.rightChild = rightChild

    print("Level-order: ", end="")
    levelOrderTraversal(newBT)
    print()
    #newNode = getDeepestNode(newBT)
    #print(newNode.data)
    #deleteDeepestNode(newBT, newNode)
    to_delete_1 = 'Hot'
    print(f"Deleting '{to_delete_1}'")
    newBT = deleteNodeBT(newBT, to_delete_1)
    print("Level-order: ", end="")
    levelOrderTraversal(newBT)
    print()
    
    print("Clear entire Binary tree called 'newBT'")
    newBT = clearBT(newBT)
    print("Level-order: ", end="")
    levelOrderTraversal(newBT)
    print()

    print("Inserted node called 'Nayeel' to 'newBT' BT")
    newBT = insertNodeBT(newBT, TreeNode('Nayeel'))
    print("Level-order: ", end="")
    levelOrderTraversal(newBT)
    print()

    print("Deleting Binary tree named 'newBT'")
    del newBT

    try:
        print(newBT)
    except UnboundLocalError:
        print("UnboundLocalError: local variable 'newBT' referenced before assignment", file=sys.stderr)
    except:
        print("Some unknown error, file=sys.stderr")

    '''


    '''
    BT2 = TreeNode('Hello')
    newNode2 = getDeepestNode(BT2)
    print(newNode2.data)

    deleteDeepestNode(BT2, newNode2)
    
    #print(deleteNodeBT(BT2, 'Hello'))
    print("Level-order: ", end="")
    levelOrderTraversal(BT2)
    print()

    insertNodeBT(BT2, TreeNode("gang"))
    print("Level-order: ", end="")
    levelOrderTraversal(BT2)
    print()
    '''
    
    '''
    newNode = TreeNode("Cold Drink")
    print(insertNodeBT(newBT, newNode))
    
    print("Level-order: ", end="")
    levelOrderTraversal(newBT)
    print()
    '''

    """ 
    print("Pre-order: ", end="")
    preOrderTraversal(newBT)
    print()

    print("In-order: ", end="")
    inOrderTraversal(newBT)
    print()

    print("Post-order: ", end="")
    postOrderTraversal(newBT)
    print()

    print("Level-order: ", end="")
    levelOrderTraversal(newBT)
    print()
    
    print(searchBT(newBT, "Tea"))
    """

if __name__ == "__main__":
    main()
