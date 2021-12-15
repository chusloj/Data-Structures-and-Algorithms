def Print_SSSP(values, parents, source_node):

	for v in parents.keys():
		if parents[v] != -1:
			print(f"{source_node} - {v}: {values[v]}")


def Bellman_Ford(adj_list, source_node):

	nodes = {v for edge in adj_list.keys() for v in edge}

	parents = {v:-1 for v in nodes}
	values = {v:1e9 for v in nodes}

	values[source_node] = 0
	updated = False
	for _ in range(len(nodes)-1):
		for edge in adj_list:
			if values[edge[0]] + adj_list[edge] < values[edge[1]]:
				values[edge[1]] = values[edge[0]] + adj_list[edge]
				parents[edge[1]] = edge[0]
				updated = True
		if updated == False:
			break

	# last time - check for negative edge weight cycle
	if updated == True:
		for edge in adj_list:
			if values[edge[0]] + adj_list[edge] < values[edge[1]]:
				print("There exists a negative edge weight cycle.")
				return False

	Print_SSSP(values, parents, source_node)





if __name__ == "__main__":

	# we can use adj matrix for directed graph
	# see dijkstra_naive.py for adj matrix -> adj list function

	adj_list = {
			(0, 1): 6,
			(0, 2): 7,
			(1, 2): 8,
			(1, 3): -4,
			(1, 4): 5,
			(2, 3): 9,
			(2, 4): -3,
			(3, 4): 7,
			(3, 0): 2,
			(4, 1): -2
	}

	# replace_dict = {
	# 	0: 'A',
	# 	1: 'B',
	# 	2: 'C',
	# 	3: 'D',
	# 	4: 'E'
	# }

	# adj_list_2 = {}

	# for edge in adj_list:
	# 	adj_list_2[ ( replace_dict[edge[0]], replace_dict[edge[1]] ) ] = adj_list[edge]
	# print(adj_list_2)

	source_node = 0
	Bellman_Ford(adj_list, source_node)
