'''
Nayeel Imtiaz
segment_tree.py
'''

class SegmentTree:
    def __init__(self, data):
        # Initialize the segment tree with the input data array
        self.n = len(data)
        self.tree = [0] * (2 * self.n)  # Tree of size 2 * n (n leaves + n-1 internal nodes)
        self.build(data)

    def build(self, data):
        # Build the segment tree in O(n)
        # First, fill the leaves (second half of the tree array)
        # for i in range(self.n):
        #     self.tree[self.n + i] = data[i]
        # # Then, build the rest of the tree by calculating parents
        # for i in range(self.n - 1, 0, -1):
        #     self.tree[i] = min(self.tree[2 * i], self.tree[2 * i + 1])

        # insert leaf nodes in tree  
        for i in range(self.n) :  
            self.tree[self.n + i] = data[i];  
      
        # build the tree by calculating parents  
        for i in range(self.n - 1, 0, -1) :  
            self.tree[i] = min(self.tree[i << 1], self.tree[i << 1 | 1])

    def query(self, left, right):
        # Perform a range query for the minimum value between [left, right) in O(log n)
        left += self.n  # Shift indices to the leaf position
        right += self.n
        min_val = float('inf')  # Initialize result to positive infinity
        while left < right:
            if left % 2 == 1:  # If left is a right child
                min_val = min(min_val, self.tree[left])
                left += 1  # Move to the next segment
            if right % 2 == 1:  # If right is a right child
                right -= 1
                min_val = min(min_val, self.tree[right])
            left //= 2  # Move to the next level
            right //= 2
        return min_val

def main():
    data_array = [5, 22, 17, 8, 13]
    segment_tree1 = SegmentTree(data_array)
    print(f"segment_tree1: {segment_tree1.tree}")

    print(f"[1, 3): {segment_tree1.query(1, 3)}")


if __name__ == '__main__':
    main()