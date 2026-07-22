# BinaryTreeClient.py
from BinaryTreeNode import BinaryTreeNode

def print_inorder(root: "BinaryTreeNode") -> None:
    if root:
        print_inorder(root.left)
        print(root.value, end=" ")
        print_inorder(root.right)


def build_tree_single_node() -> "BinaryTreeNode":
    root = BinaryTreeNode(1)
    return root

def build_tree_three_nodes() -> "BinaryTreeNode":
    root = BinaryTreeNode(10)
    root.left = BinaryTreeNode(30)
    root.right = BinaryTreeNode(50)
    return root


def main():
    print_inorder(build_tree_single_node())
    print()

    print_inorder(build_tree_three_nodes())
    print()


if __name__ == "__main__":
    main()