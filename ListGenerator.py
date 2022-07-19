# generation of list

import random

print([i for i in "Python"])
print([i for i in range(3, 11) if i % 2 == 0])
print([x * y for x in range(3) for y in range(3)])
print([[x + y for x in range(2)] for y in range(2)])
print([(lambda i: i * i)(i) for i in range(10)])
print([random.randint(10, 100) for i in range(random.randint(5, 10))])
