import queue

def BFS_util(adj_dict, first_node, visited, bfs_output):

	q = queue.Queue()
	visited[first_node] = True
	q.put(first_node)
	while not q.empty():
		current = q.get()
		bfs_output.append(current)
		for node in adj_dict[current]:
			if visited[node] == False:
				q.put(node)
				visited[node] = True



def BFS(adj_dict):

	visited = {key:False for key in adj_dict.keys()}
	# print(visited)
	bfs_output = []

	first_node = list(adj_dict.keys())[0]
	BFS_util(adj_dict, first_node, visited, bfs_output)

	return bfs_output


if __name__ == "__main__":

	adjacency_list = {
		'A': ['B', 'C'],
		'B': ['A', 'D', 'E'],
		'C': ['A', 'E'],
		'D': ['E', 'F', 'B'],
		'E': ['D', 'F', 'B', 'C'],
		'F': ['D', 'E']
	}

	output = BFS(adjacency_list)
	print(output)
