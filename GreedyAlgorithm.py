# Greedy algorithm for radiostations thats cover all states

states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}
stations = {'kone': {'id', 'nv', 'ut'}, 'ktwo': {'wa', 'id', 'mt'}, 'kthree': {'or', 'nv', 'ca'},
            'kfour': {'nv', 'ut'}, 'kfive': {'ca', 'az'}}
final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states  # выводим только штаты которые есть в ОБОИХ сетах
        if len(covered) > len(states_covered):  # проверяем количество штатов
            best_station = station
            states_covered = covered
    states_needed -= states_covered   # удаляем найденные штаты из поиска
    final_stations.add(best_station)

print(stations.items())
print(final_stations)
