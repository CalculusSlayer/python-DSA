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
        self.groups = list(range(size))
        self.ranks = [1] * size
    
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
        
def recomender(input_pairs):
    products_map = {}
    counter = 0
    for product1, product2 in input_pairs:
        if product1 not in products_map:
            products_map[product1] = counter
            counter += 1
        if product2 not in products_map:
            products_map[product2] = counter
            counter += 1

    # print(f"products_map = {products_map}")
    union_find = UnionFind(len(products_map))
    for product1, product2 in input_pairs:
        union_find.union(products_map[product1], products_map[product2])
    
    recomendations = []
    product_ids = sorted(list(products_map))
    for index1 in range(len(product_ids)):
        for index2 in range(index1 + 1, len(product_ids)):
            if (
                union_find.find(products_map[product_ids[index1]]) !=
                union_find.find(products_map[product_ids[index2]])
            ):
                recomendations.append(
                    (
                        product_ids[index1],
                        product_ids[index2]
                    )
                )
    
    return recomendations
    

def main():
    input = [(1,3), (2,7), (3,8)]
    print(recomender(input))


if __name__ == '__main__':
    main()
