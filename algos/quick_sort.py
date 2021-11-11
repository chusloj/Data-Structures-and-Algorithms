def Partition(A, start, end):

	pivot = A[end]
	p_index = start
	for i in range(start, end):
		if A[i] <= pivot:
			A[i], A[p_index] = A[p_index], A[i]
			p_index += 1
	A[p_index], A[end] = A[end], A[p_index]

	return p_index


def QuickSort(A, start, end):
	# A is already global

	if (start >= end):
		return A

	p_index = Partition(A, start, end)

	# just to know what the array looks like before sorting begins
	# print(f"partitioned array: {A}")

	left_array_sorted = QuickSort(A, start, p_index - 1)
	right_array_sorted = QuickSort(A, p_index, end)

	return A


if __name__ == "__main__":

	A = [12, 7, 2, 9, 15, 10, 5]
	A_sorted = QuickSort(A, 0, len(A)-1)

	print(f"quick sort result: {A_sorted}")
	print(f"python sort result: {sorted(A)}")
