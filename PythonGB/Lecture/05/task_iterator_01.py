# Функция iter
# Функция iter имеет формат iter(object[, sentinel]). object является обязательным аргументом.
# Если объект не реализует интерфейс итерации через методы __iter__ или __getitem__, получим ошибку TypeError.

a = 42
# iter(a) # TypeError: 'int' object is not iterable

# Получим итератор списка

data = [2, 4, 6, 8]
list_iter = iter(data)
print(list_iter)

# Один из простейших способов получить элементы - распаковать итератор через звёздочку.

data = [2, 4, 6, 8]
list_iter = iter(data)
print(*list_iter)
print(*list_iter)

