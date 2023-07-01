#    1
# num = float(input('введите число: '))
# count = 0
# while count < num:
#     print(count)
#     count += 2

#    2

# num = float(input('введите число: '))
# STEP = 2
# limit = num - STEP
# count = -STEP
# while count < limit
#     count += STEP
#     if count % 12 == 0
#         continue
#     print(count)
#
#
#    3
#
# min_limit = 0
# max_limit = 10
# while True:
#     print('Введите число между', min_limit, 'и', max_limit, '?')
#     num = float(input())
#     if num < min_limit or num > max_limit:
#         print('Неверно')
#     else:
#         break
# print('Было введено число', num)

#    4

# min_limit = 0
# max_limit = 10
# count = 3
# num = None
#
# while count > 0:
#     print('Попытка', count)
#     count -= 1
#
#     print('Введите число между', min_limit, 'и', max_limit, '?')
#     num = float(input())
#     if num < min_limit or num > max_limit:
#         print('Неверно')
#     else:
#         break
#
# else:
#     print('Исчерпаны все попытки. Сожалею. ')
#     quit()
#
# print('Было введено число', num)


#    5
# data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# for item in data:
#     print(item)

#    6

# num = int(input('Введите число: '))
# for i in range(0, num, 2):
#     print(i) # Выводит целые числа, при вводе 13 - ввывод 0 2 4 6 8 10 12

    # 7

animals = ['cat', 'dog', 'wolf', 'rate', 'dragon']
for i, animal in enumerate(animals, start=1):
    print(i, animal)
