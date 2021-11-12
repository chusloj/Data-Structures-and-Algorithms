import math

def BinarySearch(A, target):
	
	left = 0
	right = len(A)
	while left <= right:
		mid = math.floor( (left + right) / 2 )
		if A[mid] == target:
			return mid
		elif target > A[mid]:
			left = mid + 1
		else:
			right = mid - 1
	return False


if __name__ == "__main__":

	A = [x for x in range(2, int(1e5), 2)] # large array of even numbers
	target = 5900
	result = BinarySearch(A, target)
	if (A != False):
		print(f"location of {target} in array: {BinarySearch(A, target)}.")
		print(f"proof: {A[result]}")
	else:
		print("Could not find target in array.")