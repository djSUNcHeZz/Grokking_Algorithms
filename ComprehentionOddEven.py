# print odd or even for random digit

import random

# regular version
digit = random.randint(1, 100)
if digit % 2 != 0:
    print(str(digit) + ' is odd')
else:
    print(str(digit) + ' is not odd')

# list comprehension version
digit = random.randint(1, 100)
print(str(digit) + ' is odd') if digit % 2 != 0 else print(str(digit) + ' is not odd')
