class BinaryTreeNode:
    '''
    Binary Tree class
    '''

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    
def print_tree_pre_order(root):
    if root:
        print(root.val, end=" ")
        print_tree_pre_order(root.left)
        print_tree_pre_order(root.right)


def print_tree_in_order(root):
    if root:
        print_tree_in_order(root.left)
        print(root.val, end=" ")
        print_tree_in_order(root.right)


def print_tree_post_order(root):
    if root:
        print_tree_post_order(root.left)
        print_tree_post_order(root.right)
        print(root.val, end=" ")
