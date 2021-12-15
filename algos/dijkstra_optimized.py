import heapq

def Create_Adj_List(adj_matrix):
	# list taken from lower triangular section of adj matrix
	# notice that always, j<i so the max node is always i
	# and the min is always j

	adj_list = {}
	for i in range(len(adj_matrix)):
		for j in range(i):
			if (i != j) and (adj_matrix[i][j] != 0):
				adj_list[(i, j)] = adj_matrix[i][j]

	return adj_list


def Print_SSSP(values, parents, source_node):

	for v in parents.keys():
		if parents[v] != -1:
			print(f"{source_node} - {v}: {values[v]}")


def Dijkstra_Optimized(adj_list, source_node):

	nodes = {v for edge in adj_list.keys() for v in edge}

	parents = {v:-1 for v in nodes}
	processed = set()
	values = {v:1e9 for v in nodes}

	# create priority queue - min heap
	Q = []

	values[source_node] = 0
	heapq.heappush(Q, (values[source_node], source_node))
	while not all(v in processed for v in nodes):
		min_node = heapq.heappop(Q)[1]
		processed.add(min_node)
		for v in nodes:
			if min_node != v and ((min_node, v) in adj_list.keys() or (v, min_node) in adj_list.keys()):
				min_ind = min(min_node, v)
				max_ind = max(min_node, v)
				if (v not in processed) and (values[min_node] + adj_list[(max_ind, min_ind)] < values[v]):
					values[v] = values[min_node] + adj_list[(max_ind, min_ind)]
					parents[v] = min_node
					heapq.heappush(Q, (values[v], v))


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

	if not type(adj_matrix) == dict:
		adj_list = Create_Adj_List(adj_matrix)
	else:
		adj_list = adj_matrix

	source_node = 0
	Dijkstra_Optimized(adj_list, source_node)

