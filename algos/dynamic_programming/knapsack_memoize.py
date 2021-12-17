import numpy as np

def Knapsack_Memoize(weight, profit, W, N, mem):

	# if we can't fit anything in the knapsack or
	# if we consider all possible elements we have available then
	# return 0 profit
	if N < 0 or W == 0:
		return 0

	if mem[N+1][W] >= 0: # if memoize table entry is empty
		print("Memoize table accessed.")
		return mem[N+1][W]
	

	if weight[N] > W:
	# don't choose the item
		result = Knapsack_Memoize(weight, profit, W, N-1, mem)
	else:
	# POSSIBLY choose the item
		result = max(
			Knapsack_Memoize(weight, profit, W, N-1, mem), # DEFINETLY don't choose the item
			profit[N] + Knapsack_Memoize(weight, profit, W-weight[N], N-1, mem)) # DEFINETLY choose the next item

	mem[N+1][W] = result
	return result


if __name__ == "__main__":

	weight = [4, 3, 5]
	profit = [7, 6, 11] 
	W = 10

	mem = [[-1 for _ in range(W + 1)] for _ in range(len(weight) + 1)]

	total_N = 1 # start out by using only one item
	result = Knapsack_Memoize(weight, profit, W, len(weight) - 1, mem)
	print(result)
