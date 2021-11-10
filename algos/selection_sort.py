def selection_sort(A, n):
	for i in range(0, n-2): # If you sort the first n-1 elements, then then n'th element is already sorted
		imin = i
		for j in range(i+1, n-1):
			if A[j] < A[imin]:
				imin = j # index assignment minimizes cost (even though array element swapping is constant time)
		A[i], A[imin] = A[imin], A[i]
	return A

if __name__ == "__main__":
	A = [6, 2, 8, 5, 4, 10]
	A_sorted = selection_sort(A, len(A))
	print(A_sorted)