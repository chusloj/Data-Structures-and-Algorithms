import numpy as np

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


def Create_Adj_List(adj_matrix):

	adj_list = {}
	for i in range(len(adj_matrix)):
		for j in range(i):
			if (i != j) and (adj_matrix[i][j] != 0):
				adj_list[(i, j)] = adj_matrix[i][j]

	# sort edges by value
	sorted_adj_items = sorted(adj_list.items(), key=lambda x: x[1])
	sorted_adj_list = [x[0] for x in sorted_adj_items]

	return sorted_adj_list


def Iterate_Edges(node_list, edge_list):
	# NOTE: This is just Detect_Cycle_Undirected_Graph_Optimized
	# but it also processes edges

	edge_count = 0
	edge_list_final = []

	for edge in edge_list:
		if Find_Compressed_Operation(node_list, edge) == False:
			node_list = Union_Rank_Operation(node_list, edge)
			edge_list_final.append(edge)
			edge_count += 1
		if edge_count == len(adj_matrix) - 1: # for graph with V vertices, THERE ARE V - 1 EDGES!!!
			Print_MST(adj_matrix, edge_list_final)
			return
			


def Print_MST(adj_matrix, edge_list):

	for edge in edge_list:
		print(f"{edge[0]} - {edge[1]}: {adj_matrix[edge[0]][edge[1]]}")



def Kruskal_MST(adj_matrix):

	adj_list = Create_Adj_List(adj_matrix)
	node_list = [PathNode(parent = -1, rank = 0) for _ in range(len(adj_matrix))]

	Iterate_Edges(node_list, adj_list)



if __name__ == "__main__":

	adj_matrix = [
					[0, 1, 2, 0, 0, 0],
					[1, 0, 3, 1, 3, 0],
					[2, 3, 0, 2, 1, 0],
					[0, 1, 2, 0, 2, 4],
					[0, 3, 1, 2, 0, 3],
					[0, 0, 0, 4, 3, 0]
				]

	assert np.allclose(np.matrix(adj_matrix), np.matrix(adj_matrix).T)

	Kruskal_MST(adj_matrix)

