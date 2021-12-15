def Print_SSSP(values, parents, source_node):

	for v in parents.keys():
		if parents[v] != -1:
			print(f"{source_node} - {v}: {values[v]}")


def Select_Min_Node(values, processed):

	remaining_nodes = {key:value for key, value in values.items() if key not in processed}
	min_node = min(remaining_nodes, key=lambda x: remaining_nodes[x])

	return min_node


def Dijkstra_Naive(adj_matrix, source_node):

	nodes = {v for v in range(len(adj_matrix))}

	parents = {v:-1 for v in nodes}
	processed = set()
	values = {v:1e9 for v in nodes}

	values[source_node] = 0
	while not all(v in processed for v in nodes):
		min_node = Select_Min_Node(values, processed)
		processed.add(min_node)
		for v in nodes:
			if (adj_matrix[min_node][v] != 0) and (v not in processed) and (values[min_node] + adj_matrix[min_node][v] < values[v]):
				values[v] = values[min_node] + adj_matrix[min_node][v]
				parents[v] = min_node

	Print_SSSP(values, parents, source_node)



if __name__ == "__main__":

	adj_matrix = [
					[0, 1, 4, 0, 0, 0],
					[1, 0, 4, 2, 7, 0],
					[4, 4, 0, 3, 5, 0],
					[0, 2, 3, 0, 4, 6],
					[0, 7, 5, 4, 0, 7],
					[0, 0, 0, 6, 7, 0]

				]

	source_node = 0
	Dijkstra_Naive(adj_matrix, source_node)
