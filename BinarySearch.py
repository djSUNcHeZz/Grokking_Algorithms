# binary search index of number in sorted list

from random import randint


def binary_search(list, item):
    low = 0  # low limit index of list
    high = len(list) - 1  # high limit index of list

    while low <= high:
        mid = int((low + high) / 2)  # get middle number in sorted list
        guess = list[mid]
        print("I say:", guess)

        if guess == item:
            return mid

        if guess > item:  # guess too big
            print("to big")
            high = mid - 1
        else:  # guess too small
            print("to small")
            low = mid + 1

    return None  # item not found


sorted_list = [i for i in range(0, randint(10, 20), 2)]

print(sorted_list)
print("OK, index of number =", binary_search(sorted_list, int(input("search_number: "))))
