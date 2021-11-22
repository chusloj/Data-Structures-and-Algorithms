def DetectCycleUndirectedUtil(adj_list, current_node, visited_array):

	if visited_array[current_node] == 2:
		return True

	visited_array[current_node] = 1

	for adj_node in adj_list[current_node]:
		if visited_array[adj_node] == 1:
			visited_array[adj_node] = 2
		else:
			if DetectCycleUndirectedUtil(adj_list, adj_node, visited_array):
				return True
			if visited_array[adj_node] == 2:
				visited_array[adj_node] = 1


	visited_array[current_node] = 0
	return False

def DetectCycleUndirected(adj_list):

	cycle_detected = False
	visited_array = {key:0 for key in adj_list.keys()}

	for node in adj_list.keys():
		visited_array[node] = 1
		for adj_node in adj_list[node]:
			if DetectCycleUndirectedUtil(adj_list, adj_node, visited_array):
				return True
		visited_array[node] = 0
	return False


if __name__ == "__main__":

	adj_list = {
		0: [1, 2, 3],
		1: [0],
		2: [0, 3],
		3: [2, 0]
	}

	print(DetectCycleUndirected(adj_list))
	