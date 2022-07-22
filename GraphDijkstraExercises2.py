# Dijkstra graph search algorithm (exercises B)

graph = {'start': {'a': 10}, 'a': {'b': 20}, 'b': {'c': 1, 'fin': 30}, 'c': {'a': 1}, 'fin': {}}
infinity = float('inf')
parents = {'a': 'start', 'fin': None}
costs = {'a': graph['start']['a'], 'b': infinity, 'c': infinity, 'd': infinity, 'fin': infinity}


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


processed = []
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print('graph:', graph)
print('start to fin cost =', costs.get('fin'))
