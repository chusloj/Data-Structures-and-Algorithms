def Floyd_Warshall(adj_matrix):

	dist_matrix = adj_matrix

	nodes = {v for v in range(len(adj_matrix))}

	for k in nodes:
		for i in nodes:
			for j in nodes:
				if dist_matrix[i][k] is None or dist_matrix[k][j] is None:
					continue
				elif dist_matrix[i][j] is None:
					dist_matrix[i][j] = dist_matrix[i][k] + dist_matrix[k][j]
				else:
					dist_matrix[i][j] = min(dist_matrix[i][j], dist_matrix[i][k] + dist_matrix[k][j])

	for v in nodes:
		if dist_matrix[v][v] < 0:
			print("There exists a negative edge weight cycle.")
			return False

	return dist_matrix


if __name__ == "__main__":

	adj_matrix = [
		[0, 3, None, 5],
		[2, 0, None, 8],
		[None, 1, 0, None],
		[None, None, 2, 0]
	]

	result = Floyd_Warshall(adj_matrix)
	print(result)
