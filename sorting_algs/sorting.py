import math
INF = math.inf

def bubbleSort(A):
	for i in range(len(A)):
		for j in range(len(A)-i-1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]

def test_bubbleSort(A):
	print(f"Before: {A}")
	bubbleSort(A)
	print(f"After: {A}")
	print()

def selectionSort(A):
	for i in range(len(A)):
		min_index = i
		for j in range(i+1, len(A)):
			if A[min_index] > A[i]:
				min_index = j
		A[i], A[min_index] = A[min_index], A[i]

def insertion_sort(A):
	'''
		// Sorts array A in place.
		// Arrays are 1-indexed in pseudo.

		for j = 2 to A.length
				key = A[j]
				i = j-1
				while i > 0 and A[i] > key
						A[i+1] = A[i]
						i -= 1
				A[i+1] = key

	'''

	for j in range(1, len(A)):
		key = A[j]
		i = j - 1
		while i >= 0 and A[i] > key:
			A[i+1] = A[i]
			i -= 1
		A[i+1] = key


def test_insertion_sort(A):
	print(f"Before: {A}")
	insertion_sort(A)
	print(f"After: {A}")
	print()


def merge(A, p, q, r):
	'''
	A: array to pass in
	p: index of first element in subarray
	q: floor((p+r)/2)
	r: index of last element in subarray

	subarray 1 is from indices [p, q]
	subarray 2 is from indices [q+1, r]
	'''

	n1 = q - p + 1
	n2 = r - q
	L = [0 for i in range(n1+1)]
	R = [0 for j in range(n2+1)]

	for i in range(n1):
		L[i] = A[p + i]
	for j in range(n2):
		R[j] = A[q + 1 + j]

	L[n1] = INF
	R[n2] = INF

	print(f"L = {L}")
	print(f"R = {R}")
	i, j = 0, 0
	for k in range(p, r+1):
		if L[i] <= R[j]:
			A[k] = L[i]
			i = i + 1
		else:
			A[k] = R[j]
			j += 1
			#print(A, i, j)
	print(f"A = {A}, p = {p}, r = {r}")
	# k - p elements in the subarray.
	# After the loop terminates,
	# k = r + 1, so k - p = (r+1) - p elements in subarray

def merge_sort(A, p, r):
	if p < r:
		q = math.floor((p+r)/2)
		merge_sort(A, p, q)
		merge_sort(A, q+1, r)
		merge(A, p, q, r)

'''

'''


def main():
	# a1 = [1, 2, 3, 4, 5]
	a2 = [2, 1, 5, 3, 4]
	# a3 = []
	# a4 = [-5]
	# a5 = [1, 3]
	# a6 = [2, 1]

	test_bubbleSort(a2)

	a7 = [10, 5, -4, 3, 9, 10, 12]
	print(a7)
	merge_sort(a7, 0, len(a7)-1)
	print(a7)
	# test_insertion_sort(a1)
	# test_insertion_sort(a2)
	# test_insertion_sort(a3)
	# test_insertion_sort(a4)
	# test_insertion_sort(a5)
	# test_insertion_sort(a6)

	#b1 = [5, 7, 3, 1, 12, 6]
	#merge_sort(b1, 0, len(b1)-1)

	#print(f"sorted b1 = {b1}")
	# print(b1)
	# merge(b1, 0, 2, 5)
	# print(b1)
	# print()

	# b2 = [10, 20, 30, 1, 25]
	# print(b2)
	# merge(b2, 0, 2, 4)
	# print(b2)


if __name__ == "__main__":
	main()
