def Topo_Sort_Util(current_node, adj_list, visited, topo_stack):

	visited[current_node] = True

	for adj_node in adj_list[current_node]:
		if visited[adj_node] == False:
			Topo_Sort_Util(adj_node, adj_list, visited, topo_stack)

	topo_stack.append(current_node)


def Topo_Sort(adj_list):

	visited = {key:False for key in adj_list}
	topo_stack = []

	for node in adj_list:
		if visited[node] == False:
			Topo_Sort_Util(node, adj_list, visited, topo_stack)

	return topo_stack[::-1]


if __name__ == "__main__":

	adj_list = {
		5: [0, 2],
		4: [2, 1],
		0: [2, 3],
		3: [1],
		1: [],
		2: []
	}

	result = Topo_Sort(adj_list)
	print(result)

