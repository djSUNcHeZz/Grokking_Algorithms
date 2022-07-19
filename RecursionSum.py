# Recursion sum of array

from random import randint


def summary(array):
    print(array)
    return 0 if not array else array[0] + summary(array[1:])
    #  return 0 if not array else array.pop(0) + summary(array) #pop element with index 0
    #  return 0 if not array else 1 + summary(array[1:]) #count elements in array


print(summary([randint(0, 10) for i in range(randint(0, 10))]))
