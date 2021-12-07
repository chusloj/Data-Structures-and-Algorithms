def Find(set_list, start_num):

	found = False
	walker_ind = start_num
	while found != True:
		walker_result = set_list[walker_ind]
		if walker_result == -1:
			found = True
		else:
			walker_ind = walker_result


	return walker_ind

def Find_Operation(set_list, start_items):

	start_num_1, start_num_2 = start_items
	root_1 = Find(set_list, start_num_1)
	root_2 = Find(set_list, start_num_2)

	if root_1 == root_2:
		return True
	else:
		return False

def Union_Operation(set_list, set_items):

	start_num_1, start_num_2 = set_items
	root_1 = Find(set_list, start_num_1)
	root_2 = Find(set_list, start_num_2)

	set_list[root_1] = root_2

	return set_list


def Detect_Cycle_Undirected_Graph(node_list, edge_list):

	for edge in edge_list:
		if Find_Operation(node_list, edge) == True:
			return edge
		else:
			node_list = Union_Operation(node_list, edge)

	return False
			




if __name__ == "__main__":

	set_list = [None, 2, 3, -1, -1, 3, -1, 6, 6]
	print(Find_Operation(set_list, (1, 4)))
	print(Find_Operation(set_list, (2, 5)))
	print(Find_Operation(set_list, (5, 8)))

	set_list_2 = [None, 2, 3, -1, 5, 6, -1]
	print(Union_Operation(set_list_2, (1, 5)))

	node_list = [-1, -1, -1, -1]
	edge_list = [(0, 1),
				 (0, 3),
				 (2, 3),
				 (1, 2)
				 ]

	print(Detect_Cycle_Undirected_Graph(node_list, edge_list))
