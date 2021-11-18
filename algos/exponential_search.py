import math

def binary_search(A, target):
	
	left = 0
	right = len(A) - 1
	while left <= right:
		mid = math.floor( (left + right) / 2 )
		if A[mid] == target:
			return mid
		elif target > A[mid]:
			left = mid + 1
		else:
			right = mid - 1
	return False

def exponential_search(A, x):
	n = len(A)
	i = 1
	while (i < n) and (A[i] <= x):
		if A[i] == x:
			return True
		i = i*2
	start_ind = math.floor(i/2)
	end_ind = min(i, n-1)
	B = A[start_ind:end_ind+1]
	
	# correct for offset created with 0-based index in binary search
	result_ind = binary_search(B, x) + start_ind

	return result_ind # you have to return something


if __name__ == "__main__":
	
	A = [x for x in range(1,12+1)]
	print(exponential_search(A, 11))