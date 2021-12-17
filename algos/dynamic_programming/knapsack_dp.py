def Knapsack_DP(weight, profit, W):
	dp = [[-1 for _ in range(W+1)] for _ in range(len(weight) + 1)]

	for i in range(len(weight) + 1):
		for j in range(W+1):
			if i == 0 or j == 0: # knapsack has no remaining space or i < 1 (table row 1 corresponds to weight array index 0)
				dp[i][j] = 0
			elif weight[i-1] > j: # skip the item
				dp[i][j] = dp[i-1][j]
			else: # possibly consider the value
				dp[i][j] = max(dp[i-1][j], profit[i-1] + dp[i-1][j - weight[i-1]])

	return dp[len(weight)][W]


if __name__ == "__main__":

	weight = [1, 2, 3]
	profit = [2, 3, 5]
	W = 4

	# weight = [4, 3, 5]
	# profit = [7, 6, 11] 
	# W = 10

	result = Knapsack_DP(weight, profit, W)
	print(result)