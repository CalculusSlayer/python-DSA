# Nayeel Imtiaz
# quickSort.py
# Quick Sort program in Python
# Inspired from "Introduction to Algorithms 3rd edition" [CLRS pg. 71]

def partition(A, p, r):
    '''
    Helper function for main quicksort function
    '''
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def quicksort(A, p, r):
    '''
    main quick sort function implementation
    '''
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

def main():
	a1 = [5, 9, 2, 99, 1, 2, 3, 8, 9, 10, 11, 33, 3, 1, 5, 9, 17, 18, 5, 9]
	print(a1)
	quicksort(a1, 0, len(a1)-1)
	print(a1)

if __name__ == '__main__':
	main()