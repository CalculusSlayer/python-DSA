# UnionFind.py
# - Contains code for Union Find
# data structure.
# Nayeel Imtiaz
# 1/3/22

# Beginning of UnionFind class
class UnionFind:
    def __init__(self, size):
        '''
        Initializer function. Creates a Union
        Find (also called disjoint set) object.

        Return:
                (UnionFind) A `UnionFind` object.

        Params:
                size (int) - The number of elements to
                be in the Union Find structure

        Instance variables:
                size (int) - Number of elements in Union
                Find structure

                numComponents (int) - The number of components
                /groups in the Union Find.

                sz (list[int]) - A fix sized list that keeps track
                of the sizes of each component.

                id (list[int]) - A fix sized list that keeps track of
                the current parent of each element.
        '''
        # TODO: Add code to throw an exception
        # when size is less than or equal to 0.

        self.size = self.numComponents = size
        self.sz = [1 for i in range(size)]
        self.id = [i for i in range(size)]

    def __repr__(self):
        return (f"size = {self.size}, "
                f"number of components = {self.numComponents}, "
                f"size array = {self.sz}, "
                f"parents array = {self.id}")

    def find(p):
        '''
        Function finds out which component
        element `p` is in. Then it does
        path compression to optimize
        the Union Find structure.

        Return:
                (int) The root of element `p`.

        Params:
                p (int) - An element in the Union Find.
        '''

        # Finding root element of the component
        # element p is contained in.
        root = p
        while root != id[root]:
            root = id[root]

        # Path compression. All elements from p
        # to root will now point to the root.
        # This gives us amortized time complexity.
        while p != root:
            next = id[p]
            id[p] = root
            p = next

        return root

    def connected(p, q):
        '''
        Return true or false base on whether
        p and q are in the same component or not.

        Return:
        (boolean) True or False.

        Params:
        p (int) - Element 1
        q (int) - Element 2
        '''
        return find(p) == find(q)

    def componentSize(p):
        '''
        Return the size of the component
        element p is contained in.

        Return:
                (int) Size of the component element p
                is contained in as an integer.

        Params:
                p (int) - Element

        '''
        return sz[find(p)]

    def size():
        '''
        Return the number of elements in
        this UnionFind.

        Return:
                (int) Number of elements in
                the UnionFind.

        Params:
                None
        '''
        return self.size

    def components():
        '''
        Return the number of components in
        this UnionFind.

        Return:
                (int) Number of components in
                this UnionFind.

        Params:
                None
        '''
        return self.components

    def unify(p, q):
        '''
        Unify the sets containing elements
        `p` and `q`.

        Return:
                None

        Params:
                p (int) - A

        '''

        if self.connected(p, q):
            return

        root1 = find(p)
        root2 = find(q)

        if sz[root1] < sz[root2]:
            sz[root2] += sz[root1]
            id[root1] = root2
            sz[root1] = 0

        else:
            sz[root1] += sz[root2]
            id[root2] = root1
            sz[root2] = 0

        self.numComponents -= 1

# End of UnionFind class
