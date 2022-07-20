#  Gragh seearch use deque()


from collections import deque

graph = {'you': ['alice', 'bob', 'claire'], 'bob': ['anuj', 'peggy'], 'alice': ['peggy'], 'claire': ['thom', 'jonny'],
         'anuj': [], 'peggy': [], 'thom': [], 'jonny': []}


def person_is_saller(person):  # функция проверки продавца манго по последней букве
    return person[-1] == search_name  # search last letter in name


def graph_search_deque():
    search_queue = deque()  # создать двустороннюю очередь
    search_queue += graph['you']  # добавить первых ближайших в очередь
    while search_queue:
        person = search_queue.popleft()  # вытащить первого из очереди
        if person_is_saller(person):  # вызвать функцию проверки продавца манго
            print(person + ' is mango seller')
            return True
        else:
            search_queue += graph[person]  # добавить соседей следующего уровня если не нашли
    print('No mango sellers')
    return False


search_name = input('Search name: ')
print(graph_search_deque())
