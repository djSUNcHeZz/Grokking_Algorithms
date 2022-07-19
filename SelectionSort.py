# Selection sort of random list using sorted_arr
from random import randint


def find_smaller_index(arr):  # return smallest index in array
    smallest, smallest_index = arr[0], 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest, smallest_index = arr[i], i
    return smallest_index


def selection_sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        smallest_index = find_smaller_index(arr)
        sorted_arr.append(arr.pop(smallest_index))  # pop element from arr and append to sortedArr
        print("arr:", arr)
        print("sortedArr:", sorted_arr)
    return sorted_arr


randomList = [randint(0, 10) for i in range(randint(5, 15))]
print("Random list:", randomList)
print("Sorted list:", selection_sort(randomList))
