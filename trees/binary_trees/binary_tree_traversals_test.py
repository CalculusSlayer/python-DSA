# binary_tree_traversals_test.py
import pytest
from binary_tree import BinaryTreeNode, print_tree_pre_order, print_tree_in_order, print_tree_post_order

def create_standard_binary_tree():
    root_node = BinaryTreeNode("root")
    node_1 = BinaryTreeNode(1)
    node_2 = BinaryTreeNode(2)
    root_node.left = node_1
    root_node.right = node_2

    node_3 = BinaryTreeNode(3)
    node_4 = BinaryTreeNode(4)
    node_5 = BinaryTreeNode(5)
    node_6 = BinaryTreeNode(6)
    node_1.left = node_3
    node_1.right = node_4
    node_2.left = node_5
    node_2.right = node_6

    return root_node


def test_preorder_traversal(capsys):
    tree = create_standard_binary_tree()
    print_tree_pre_order(tree)
    captured = capsys.readouterr()
    assert captured.out == "root 1 3 4 2 5 6 "


def test_inorder_traversal(capsys):
    tree = create_standard_binary_tree()
    print_tree_in_order(tree)
    captured = capsys.readouterr()
    assert captured.out == "3 1 4 root 5 2 6 "


def test_postorder_traversal(capsys):
    tree = create_standard_binary_tree()
    print_tree_post_order(tree)
    captured = capsys.readouterr()
    assert captured.out == "3 4 1 5 6 2 root "
