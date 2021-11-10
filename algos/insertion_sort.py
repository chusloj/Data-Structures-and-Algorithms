def insertion_sort(A, n):
	for i in range(1, n):
		val = A[i]
		walker = i
		while (walker > 0 and A[walker - 1] > val):
			A[walker] = A[walker-1]
			walker -= 1
		A[walker] = val
	return A

if __name__ == "__main__":
	A = [3, 6, 9, 5, 7, 4, 2, 14]
	size = len(A)
	print(insertion_sort(A, size))