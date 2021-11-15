# Heapsort algorithm + data structure

import math

def MaxHeapify(A, ind, heapsize):

	left_ind = 2*ind + 1
	right_ind = 2*ind + 2
	if (left_ind < heapsize) and (A[left_ind] > A[ind]):
		largest_ind = left_ind
	else:
		largest_ind = ind

	if (right_ind < heapsize) and (A[right_ind] > A[largest_ind]):
		largest_ind = right_ind

	# This disconnected if statement ensures that largest selects the maximum
	# of parent, left child and right child
	if largest_ind != ind:
		A[ind], A[largest_ind] = A[largest_ind], A[ind]
		MaxHeapify(A, largest_ind, heapsize)

def BuildMaxHeap(A):

	for i in range(math.floor(len(A) / 2) - 1, 0 - 1, -1):
		MaxHeapify(A, i, len(A))

def ExtractMax(A):

	max_elem = A[0]
	A[0] = A.pop()
	MaxHeapify(A, 0, len(A))

	return max_elem

def IncreaseNodeValue(A, node, new_value):

	if new_value < A[node]:
		return

	A[node] = new_value
	ind = node
	while(ind < 0 and A[math.floor(ind / 2)] < A[ind]):
		A[A[math.floor(ind / 2)]], A[ind] = A[ind], A[math.floor(ind / 2)]
		ind = math.floor(ind / 2)

def DecreaseNodeValue(A, node, new_value):

	if new_value > A[node]:
		return

	A[node] = new_value
	MaxHeapify(A, node, len(A))

def InsertValue(A, new_value):

	A[len(A)] = new_value
	ind = len(A)
	while(ind < 0 and A[math.floor(ind / 2)] < A[ind]):
		A[A[math.floor(ind / 2)]], A[ind] = A[ind], A[math.floor(ind / 2)]
		ind = math.floor(ind / 2)

def HeapSort(A):

	BuildMaxHeap(A)

	for i in range(len(A) - 1, 0, -1):
		A[0], A[i] = A[i], A[0]
		MaxHeapify(A, 0, heapsize=i-1)


if __name__ == "__main__":

	A = [13, 6, 9, 4, 2, 3, 1, 5, 8]

	HeapSort(A)
	print(A)
