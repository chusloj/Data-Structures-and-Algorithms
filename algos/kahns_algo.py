import queue

def Kahn(adj_list):

	node_queue = queue.Queue()

	# step 1: find indegree
	indegree_count = {key:0 for key in adj_list}
	for node in adj_list:
		for adj_node in adj_list[node]:
			indegree_count[adj_node] += 1

	# step 2: add nodes with indegree == 0 to queue
	# minimum indegree is = 0
	for key in indegree_count.keys():
		if indegree_count[key] == 0:
			node_queue.put(key)
	
	# step 3: process queue
	node_count = 0
	nodes_sorted = []
	while not node_queue.empty():
		current_node = node_queue.get()
		for adj_node in adj_list[current_node]:
			indegree_count[adj_node] -= 1
			if indegree_count[adj_node] == 0:
				node_queue.put(adj_node)
		nodes_sorted.append(current_node)
		node_count += 1

	if node_count == len(adj_list.keys()):
		return nodes_sorted
	else:
		ValueError("There is a cycle or there has been an error.")


if __name__ == "__main__":

	adj_list = {
		5: [0, 3],
		4: [0, 1],
		0: [],
		3: [0, 2],
		1: [],
		2: [1]
	}

	result = Kahn(adj_list)
	print(result)

