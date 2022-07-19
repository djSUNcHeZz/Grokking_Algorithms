# View graph keys

# graph = {'you': ['alice', 'bob', 'claire'], 'bob': ['anuj', 'peggy'], 'alice': ['peggy'], 'claire': ['thom', 'jonny'],
#          'anuj': [], 'peggy': [], 'thom': [], 'jonny': []}

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


def check_input_name():
    graph_name = input('Input graph name: ')
    print(graph[graph_name]) if graph.get(graph_name) is not None else check_input_name()


check_input_name()
