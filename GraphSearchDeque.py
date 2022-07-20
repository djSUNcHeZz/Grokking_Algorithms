#  Gragh seearch use deque()


from collections import deque

graph = {'you': ['alice', 'bob', 'claire'], 'bob': ['anuj', 'peggy'], 'alice': ['peggy'], 'claire': ['thom', 'jonny'],
         'anuj': [], 'peggy': [], 'thom': [], 'jonny': []}


def person_is_saller(person):  # функция проверки продавца манго по последней букве (return True/False)
    return person[-1] == search_in_name  # search last letter in name


def graph_search_deque(first_search_name):
    search_queue = deque()  # создать двустороннюю очередь
    search_queue += graph[first_search_name]  # добавить первых ближайших в очередь
    searched = []  # массив проверенных людей для исключения зацикливания
    while search_queue:
        person = search_queue.popleft()  # вытащить первого из очереди
        if person_is_saller(person):  # вызвать функцию проверки продавца манго
            print(person + ' is mango seller')
            return True
        else:
            search_queue += graph[person]  # добавить соседей следующего уровня если не нашли
            searched.append(person)  # добавить узел в проверенные
    print('No mango sellers')
    return False


first_search_name = input('First search name: ')
search_in_name = input('Search last letter in name: ')
print(graph_search_deque(first_search_name))
