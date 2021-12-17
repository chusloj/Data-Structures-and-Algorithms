def Knapsack_Recursion(weight, profit, W, N):

	# if we can't fit anything in the knapsack or
	# if we consider all possible elements we have available then
	# return 0 profit
	if N < 0 or W == 0:
		return 0
	

	if weight[N] > W:
	# don't choose the item
		return Knapsack_Recursion(weight, profit, W, N-1)
	else:
	# POSSIBLY choose the item
		return max(
			Knapsack_Recursion(weight, profit, W, N-1), # DEFINETLY don't choose the item
			profit[N] + Knapsack_Recursion(weight, profit, W-weight[N], N-1)) # DEFINETLY choose the next item


if __name__ == "__main__":

	# weight = [3, 2, 4]
	# profit = [6, 8, 7]
	# W = 8

	# weight = [3, 2, 4]
	# profit = [8, 5, 9]
	# W = 7

	weight = [4, 3, 5]
	profit = [7, 6, 11]
	W = 10

	result = Knapsack_Recursion(weight, profit, W, len(weight) - 1)
	print(result)
