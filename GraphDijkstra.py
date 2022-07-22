# Dijkstra graph search algorithm


# graph = {}
# graph['start'] = {}
# graph['start']['a'] = 6
# graph['start']['b'] = 2
# graph['a'] = {}
# graph['a']['fin'] = 1
# graph['b'] = {}
# graph['b']['a'] = 3
# graph['b']['fin'] = 5
# graph['fin'] = {}

graph = {'start': {'a': 6, 'b': 2}, 'a': {'fin': 1}, 'b': {'a': 3, 'fin': 5}, 'fin': {}}
infinity = float('inf')  # бесконечность
costs = {'a': 6, 'b': 2, 'fin': infinity}  # стоимости обновляются в процессе
parents = {'a': 'start', 'b': 'start', 'fin': None}  # родители узла обновляются в процессе


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

# dictionary commands:
# print(graph.keys())
# print(graph.values())
# print(graph.items())
# print(graph.get('start'))
# print(graph.items())
# print(graph.pop('start'))
# print(graph.items())
# print('a' in graph)
