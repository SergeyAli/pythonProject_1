# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
count = 10
num_1 = None
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)

while count > 0:
    print('Осталось ', count, ' попыткок')
    count -= 1

    print('Введите число между', LOWER_LIMIT, 'и', UPPER_LIMIT, '!')
    num_1 = float(input())
    # if num < LOWER_LIMIT or num > UPPER_LIMIT:
    if num != num_1:
         if num > num_1:
            print('Задуманное число больше чем: ', num_1)
         else:
             print('Задуманное число меньше: ', num_1)
    else:
         break

else:
    print('Исчерпаны все попытки. Сожалею. ')
    quit()

print('Вы угадали, было задумано число: ', num)