'''
Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса
'''

from task_1 import fun_top
from task_2 import fun_secret
from task_5 import guess_number
from task_6 import guess_number_


if __name__ == '__main__':
    game = fun_top(100, 5)
    game()
    fun_secret(50, 8)
    guess_number(5)
    guess_number_(5)