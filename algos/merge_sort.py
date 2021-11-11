import math

def MergeTogether(A, left_array, right_array):

	left_n = len(left_array)
	right_n = len(right_array)
	i = j = k = 0
	while (i < left_n) and (j < right_n):
		if left_array[i] <= right_array[j]:
			A[k] = left_array[i]
			i += 1
		else:
			A[k] = right_array[j]
			j += 1
		k += 1
	# now, one of the walkers can reach the end of the array first...
	while i < left_n:
		A[k] = left_array[i]
		k += 1
		i += 1
	while j < right_n:
		A[k] = right_array[j]
		k += 1
		j += 1

	return A


def MergeSort(A):

	if (len(A) <= 1):
		return A
	midpoint = math.floor(len(A)/2)
	left_array = A[0:midpoint]
	right_array = A[midpoint:len(A)]
	left_array_sorted = MergeSort(left_array)
	right_array_sorted = MergeSort(right_array)
	A_sorted = MergeTogether(A, left_array_sorted, right_array_sorted)

	return A_sorted


if __name__ == "__main__":
	
	A = [7, 3, 1, 4, 9, 14, 10]
	A_sorted = MergeSort(A)

	print(f"merge sort result: {A_sorted}")
	print(f"python sort result: {sorted(A)}")
