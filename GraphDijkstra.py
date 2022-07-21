# Dijkstra graph search algorithm

graph = {'start': {'a': 6, 'b': 2}, 'a': {'fin': 1}, 'b': {'a': 3, 'fin': 5}, 'fin': {}}
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
infinity = float('inf')  # бесконечность
costs = {'a': 6, 'b': 2, 'fin': infinity}  # стоимости обновляются в процессе
parents = {'a': 'start', 'b': 'start', 'fin': None}  # родители узла обновляются в процессе

print(graph.keys())
print(graph.values())
print(graph.items())
print(graph.get('start'))
print(graph.items())
print(graph.pop('start'))
print(graph.items())
print('a' in graph)

# print(graph.keys())
