def Select_Min_Vertex(values, mst_processed):

	min_node_value = 1e99
	final_node = None
	for adj_node in range(len(adj_matrix)):
		
		if (mst_processed[adj_node] == False) and (values[adj_node] < min_node_value):
			min_node_value = values[adj_node]
			final_node = adj_node

	return final_node

def Print_MST(adj_matrix, parents):

	for node in range(len(parents)):
		if parents[node] != -1:
			print(f"{node} - {parents[node]}: {adj_matrix[node][parents[node]]}")

def Find_MST(adj_matrix):

	parents = [None] * len(adj_matrix)
	mst_processed = {x:False for x in range(len(adj_matrix))}
	values = [1e99] * len(adj_matrix)

	# start at source node
	parents[0] = -1
	values[0] = 0

	while any(value == False for value in mst_processed.values()):

		current_node = Select_Min_Vertex(values, mst_processed)
		mst_processed[current_node] = True

		for adj_node in range(len(adj_matrix)):

			if (adj_matrix[current_node][adj_node] != 0) and (mst_processed[adj_node] == False) and (adj_matrix[current_node][adj_node] < values[adj_node]):
				values[adj_node] = adj_matrix[current_node][adj_node]
				parents[adj_node] = current_node

	Print_MST(adj_matrix, parents)



if __name__ == "__main__":

	adj_matrix = [
					[0, 4, 6, 0, 0, 0],
					[4, 0, 6, 3, 4, 0],
					[6, 6, 0, 1, 0, 0],
					[0, 3, 1, 0, 2, 3],
					[0, 4, 0, 2, 0, 7],
					[0, 0, 0, 3, 7, 0]
					
				]

	Find_MST(adj_matrix)
