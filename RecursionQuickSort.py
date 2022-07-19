# Recursion quick sort

from random import randint


## def quick_sort(array):
##     if array: return quick_sort([i for i in array[1:] if i < array[0]]) + [i for i in array if i == array[0]] + quick_sort([i for i in array[1:] if i > array[0]])
##     return array


### def quick_sort(array):
###     if array: return quick_sort(list(filter(lambda x: x <= array[0], array[1:]))) + array[:1] + quick_sort(list(filter(lambda x: x > array[0], array[1:])))
###     return array


def quick_sort(array):
    if not array:  # len(array) <= 1:  # базовый случай
        return array

    pivot = array[len(array) // 2]  # выбираем опорный элемент в центре массива

    sorted_center = []  # необходимо только при использовании append
    left = []  # необходимо только при использовании append
    right = []  # необходимо только при использовании append

    for i in array:  # в один проход используя append в 3 массивах
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            sorted_center.append(i)

    return quick_sort(left) + sorted_center + quick_sort(right)


array = [randint(0, 10) for i in range(randint(0, 40))]
print(array)
print(quick_sort(array))
