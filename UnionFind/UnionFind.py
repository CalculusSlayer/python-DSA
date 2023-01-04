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



	

