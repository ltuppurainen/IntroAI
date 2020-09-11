import json
import queue

with open('network.json') as file:
  stop_data = json.load(file)

graph = {}
for entry in stop_data:
	graph[entry['code']] = list(entry['neighbors'].keys())

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

		if cur_node == end:
			return paths[cur_node]
	
	return None

print(search(graph, "1250429", "1121480"))