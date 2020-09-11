import queue

graph = {

	'A': ['B'],
	'B': ['A','C','F'],
	'C': ['B','E','I'],
	'D': ['F'],
	'E': ['C'],
	'F': ['D','G'],
	'G': ['F','H'],
	'H': ['G'],
	'I': ['C']

}

def search(graph, start, end, is_dfs=False):
	visited = set()
	paths = {start: [start]}
	if is_dfs:
		q = queue.LifoQueue()
	else:
		q = queue.Queue()
	q.put(start)

	while not q.empty():
		cur_node = q.get()
		visited.add(cur_node)
		for child in graph[cur_node]:
			if child not in visited:
				q.put(child)
				paths[child] = paths[cur_node] + [child]

		print("Currently at", cur_node,", queued nodes:",list(q.queue), ", visited nodes: ", list(visited))
		if cur_node == end:
			print("Final path:", paths[cur_node])
			return True
	
	return False


if __name__ == "__main__":
	search(graph, 'A', 'I')
	print("--")
	search(graph, 'A', 'I', True)