'''
There are N products given in pairs, the pairing indicates that they belong to the same
category. 

Return a list of product pairs so that each product in the pair does not belong to 
the same category.

Essentially make recommendations for products and make sure that the recommended product
 is not the same category with the other product in the pair.

Input: [(1,3), (2,7), (3,8)]
Output: [(1,2),(1,7),(3,2),(3,7),(8,2),(8,7)]
'''
class UnionFind:
    def __init__(self, size):
        self.size = self.components = size
        self.groups = [parent for parent in range(self.size)]
        self.ranks = [1 for _ in range(self.size)]
    
    def find(self, element):
        if self.groups[element] != element:
            self.groups[element] = self.find(self.groups[element])
        return self.groups[element]

    def union(self, element1, element2):
        group1 = self.find(element1)
        group2 = self.find(element2)

        if group1 != group2:
            if self.ranks[group1] > self.ranks[group2]:
                self.groups[group2] = group1
            elif self.ranks[group1] < self.ranks[group2]:
                self.groups[group1] = group2
            else:
                self.groups[group2] = group1
                self.ranks[group1] += 1
            self.components -= 1
        
def recomender(input):
    products_map = {}
    counter = 0
    for product1, product2 in input:
        if product1 not in products_map:
            products_map[product1] = counter
            counter += 1
        if product2 not in products_map:
            products_map[product2] = counter
            counter += 1

    # print(f"products_map = {products_map}")
    union_find = UnionFind(len(products_map))
    for product1, product2 in input:
        union_find.union(products_map[product1], products_map[product2])
    
    recomendations = []
    products_map_items = list(products_map.items())
    for index1, (product1, group1) in enumerate(products_map_items):
        index2 = index1 + 1
        while index2 < len(products_map_items):
            product2, group2 = products_map_items[index2]
            if (
                (union_find.find(products_map[product1]) !=
                union_find.find(products_map[product2]))
            ):
                recomendations.append((product1, product2))
            index2 += 1
    
    return recomendations
    

def main():
    input = [(1,3), (2,7), (3,8)]
    print(recomender(input))


if __name__ == '__main__':
    main()
