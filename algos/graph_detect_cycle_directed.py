def DetectCycleDirectedUtil(adj_list, current_node, visited_array):

	visited_array[current_node] = True

	for adj_node in adj_list[current_node]:
		if visited_array[adj_node] == True:
			return True
		else:
			if DetectCycleDirectedUtil(adj_list, adj_node, visited_array):
				return True

	visited_array[current_node] = False
	return False

def DetectCycleDirected(adj_list):

	cycle_detected = False
	visited_array = {key:False for key in adj_list.keys()}

	for node in adj_list.keys():	
		cycle_detected = DetectCycleDirected(adj_list, node, visited_array)
		if cycle_detected == True:
			return True
	return False


if __name__ == "__main__":

	adj_list = {
		0: [1],
		1: [],
		2: [1, 3],
		3: [4],
		4: [0, 2]
	}

	adj_list_2 = {
		0: [1, 2],
		1: [],
		2: [3],
		3: [0]
	}

	print(DetectCycleDirected(adj_list_2))
	