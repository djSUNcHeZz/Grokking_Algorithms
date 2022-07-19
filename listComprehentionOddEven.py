# print odd or even for random list

import random

list = [random.randint(0, 9) for i in range(5)]
print("Random list:", list)
print(['even' if x % 2 == 0 else 'odd' for x in list])
