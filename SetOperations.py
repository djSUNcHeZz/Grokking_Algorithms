# Set() operations
# set - набор УНИКАЛЬНЫХ элементов
# операции | & - нельзя делать со словарями dict()


fruits = set(['avocado', 'tomato', 'banana'])
vegetables = set(['beets', 'carrots', 'tomato'])

print(fruits | vegetables)  # объединяет удаляя дубликаты
print(fruits & vegetables)  # выводит пересечение (только то что есть там И там)
print(fruits - vegetables)  # удаляет из первого те что есть во втором
