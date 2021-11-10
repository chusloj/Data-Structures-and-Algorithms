def bubble_sort(A, n):
	while True:
		change_occured = False
		for i in range(0, n-1): # if you sort n-1 elements, the nth element will be sorted
			if A[i+1] < A[i]:
				A[i+1], A[i] = A[i], A[i+1]
				change_occured = True
		if change_occured == False:
			break
	return A

if __name__ == "__main__":
	A = [3, 6, 9, 5, 7, 4]
	size = len(A)
	print(bubble_sort(A, size))