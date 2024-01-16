from binary_tree import BinaryTreeNode, print_tree_pre_order

# def invert_binary_tree_iterative(root):
    

def test1():
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

    print_tree_pre_order(root_node)


def main():
    test1()


if __name__ == '__main__':
    main()