# Assumes that nodes are numbered, not lettered or any other form.

class PathNode:

	def __init__(self, parent, rank):
		self.parent = parent
		self.rank = rank


def Find_Compressed(set_list, start_num):
	# NOTE: updating the start_num parent at each step makes sure that a find ran on an
	# absolute root just stops

	walker = start_num
	while set_list[walker].parent != -1:
		walker = set_list[walker].parent
		set_list[start_num].parent = walker

	return walker

def Find_Compressed_Operation(set_list, start_items):

	start_num_1, start_num_2 = start_items
	root_1 = Find_Compressed(set_list, start_num_1)
	root_2 = Find_Compressed(set_list, start_num_2)

	if root_1 == root_2:
		return True
	else:
		return False

def Union_Rank_Operation(set_list, set_items):

	start_num_1, start_num_2 = set_items
	root_1 = Find_Compressed(set_list, start_num_1)
	root_2 = Find_Compressed(set_list, start_num_2)

	if set_list[root_1].rank < set_list[root_2].rank:
		set_list[root_1].parent = root_2
	elif set_list[root_1].rank > set_list[root_2].rank:
		set_list[root_2].parent = root_1
	else:
		set_list[root_1].parent = root_2

	return set_list


def Detect_Cycle_Undirected_Graph_Optimized(node_list, edge_list):

	for edge in edge_list:
		if Find_Compressed_Operation(node_list, edge) == True:
			return edge
		else:
			node_list = Union_Rank_Operation(node_list, edge)

	return False
			



if __name__ == "__main__":

	set_list = [None, PathNode(-1, 2), PathNode(1, 2), PathNode(2, 2)]
	print(Find_Compressed(set_list, 3))
	print(set_list[3].parent)

	set_list_2 = [None, PathNode(-1, 2), PathNode(1, 2), PathNode(2, 2), None, PathNode(-1, 1), PathNode(5, 1)]
	# print(Find_Compressed(set_list_2, 3))
	# print(Find_Compressed(set_list_2, 6))
	set_list_2 = Union_Rank_Operation(set_list_2, (1, 5))
	print(Find_Compressed(set_list_2, 6))

	node_list = [PathNode(-1, 0) for _ in range(5)] # 4 nodes in range [0, 4]
	edge_list = [
					(0, 1),
					(2, 3),
					(1, 2),
					(0, 4),
					(4, 3)
				]

	print(Detect_Cycle_Undirected_Graph_Optimized(node_list, edge_list))
