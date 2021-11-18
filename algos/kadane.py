def Kadane(A):
	max_ending_here = 0
	max_so_far = 0
	for i in A:
		max_ending_here = max_ending_here + i
		if max_ending_here < i:
			max_ending_here = i
		if max_so_far < max_ending_here:
			max_so_far = max_ending_here

	return max_so_far

if __name__ == "__main__":

	A = [-2, -3, 4, -1, -2, 1, 5, -3]
	print(Kadane(A))