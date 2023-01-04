# UnionFind.py
# - Contains code for Union Find
# data structure.
# Nayeel Imtiaz
# 1/3/22

class UnionFind:
	def __init__(self, size):
		'''
		Initializer function. Creates a Union
		Find (also called disjoint set) object.

		Return:
			A `UnionFind` object.

		Params:
			size - The number of elements to
			be in the Union Find structure

		Instance variables:
			size - Number of elements in Union
			Find structure

			numComponents - The number of components
			/ groups in the Union Find.

			sz - A fix sized list that keeps track
			of the sizes of each component (only the
			root element of each component will contain 
			the most updated size).

			id - A fix sized list that keeps track of
			the current parent of each element.
		'''
		# TODO: Add code to throw an exception
		# when size is less than or equal to 0.

		self.size = self.numComponents = size
		self.sz = [1 for i in range(size)]
		self.id = [i for i in range(size)]


	def find(int p):
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
			True or False.

		Params:
			p - Element 1
			q - Element 2
		'''
		return find(p) == find(q)
	

