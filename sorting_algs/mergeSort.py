# Nayeel Imtiaz
# mergeSort.py
# Merge Sort program in Python
# Inspired from "Introduction to Algorithms 3rd edition" [CLRS pgs. 31-34]

def floor(n):
    return int(n // 1)

def merge(A, p, q, r):
	'''
	THIS IS A HELPER FUNCTION FOR MERGE SORT FUNCTION

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

	L[n1] = float('inf')
	R[n2] = float('inf')

	#print(f"L = {L}")
	#print(f"R = {R}")
	i, j = 0, 0
	for k in range(p, r+1):
		if L[i] <= R[j]:
			A[k] = L[i]
			i = i + 1
		else:
			A[k] = R[j]
			j += 1
			#print(A, i, j)
	#print(f"A = {A}, p = {p}, r = {r}")
	# k - p elements in the subarray.
	# After the loop terminates,
	# k = r + 1, so k - p = (r+1) - p elements in subarray

def merge_sort(A, p, r):
	'''
	Main merge sort function
	'''

	if p < r:
		q = floor((p+r)/2)
		merge_sort(A, p, q)
		merge_sort(A, q+1, r)
		merge(A, p, q, r)

def main():
	a1 = [5, 9, 2, 99, 1, 2, 3, 8, 9, 10, 11, 33, 3, 1, 5, 9, 17, 18, 5, 9]
	print(a1)
	merge_sort(a1, 0, len(a1)-1)
	print(a1)

if __name__ == '__main__':
	main()