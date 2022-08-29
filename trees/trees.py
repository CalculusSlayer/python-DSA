class TreeNode:
    def __init__(self, data, children=None):
        self.data = data
        if children == None:
            self.children = []
        else:
            self.children = children

    def __str__(self, level=0):
        ret = "  " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
        
    def addChild(self, TreeNode):
        self.children.append(TreeNode)


def main():
    tree = TreeNode('Drinks')
    cold = TreeNode('Cold')
    hot = TreeNode('Hot')
    cola = TreeNode('Cola')
    fanta = TreeNode('Fanta')
    tea = TreeNode('Tea')
    coffee = TreeNode('Coffee')

    tree.addChild(cold)
    tree.addChild(hot)

    cold.addChild(cola)
    cold.addChild(fanta)

    hot.addChild(tea)
    hot.addChild(coffee)

    superTree = TreeNode('Super Tree', [tree])

    print(superTree)


if __name__ == "__main__":
    main()
