import math

class SparseTable:
    def __init__(self, arr):
        """
        Initialize the Sparse Table with the input array.
        Preprocessing takes O(n log n) time.
        """
        self.n = len(arr)
        self.log = [0] * (self.n + 1)
        self.st = []
        self.build(arr)

    def build(self, arr):
        # Precompute logs
        for i in range(2, self.n + 1):
            self.log[i] = self.log[i // 2] + 1

        # Initialize the sparse table
        k = self.log[self.n] + 1
        self.st = [[0] * k for _ in range(self.n)]

        # Base case: intervals of length 1
        for i in range(self.n):
            self.st[i][0] = arr[i]

        # Build the sparse table
        j = 1
        while (1 << j) <= self.n:
            i = 0
            while (i + (1 << j) - 1) < self.n:
                self.st[i][j] = min(self.st[i][j - 1], self.st[i + (1 << (j - 1))][j - 1])
                i += 1
            j += 1

    def query(self, L, R):
        """
        Perform a Range Minimum Query from index L to R.
        Querying takes O(1) time.
        """
        j = self.log[R - L + 1]
        return min(self.st[L][j], self.st[R - (1 << j) + 1][j])

# Example Usage
arr = [1, 3, 2, 7, 9, 11, 3, 5, 2, 8]
st = SparseTable(arr)

# Query the minimum value in the range [2, 5]
print(st.query(2, 5))  # Output: 2
