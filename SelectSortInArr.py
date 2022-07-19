# selection sort in array

from random import randint


def select_sort(array):
    for i in range(len(array) - 1):
        for k in range(i + 1, len(array)):
            if array[k] < array[i]:
                array[k], array[i] = array[i], array[k]
    return array


array = [randint(0, 10) for i in range(0, randint(0, 20))]
print(array)
print(select_sort(array))
