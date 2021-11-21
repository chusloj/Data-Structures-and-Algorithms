def DFS_util(adj_dict, current_node, visited, dfs_output):

	visited[current_node] = True
	dfs_output.append(current_node)

	for node in adj_dict[current_node]:
		if visited[node] == False:
			DFS_util(adj_dict, node, visited, dfs_output)

def DFS(adj_dict):

	visited = {key:False for key in adj_dict.keys()}
	# print(visited)
	dfs_output = []

	first_node = list(adj_dict.keys())[0]
	DFS_util(adj_dict, first_node, visited, dfs_output)

	return dfs_output

if __name__ == "__main__":

	adjacency_list = {
		'A': ['B', 'C'],
		'B': ['A', 'D', 'E'],
		'C': ['A', 'E'],
		'D': ['E', 'F', 'B'],
		'E': ['D', 'F', 'B', 'C'],
		'F': ['D', 'E']
	}

	output = DFS(adjacency_list)
	print(output)