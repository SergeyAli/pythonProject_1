'''
Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
'''
import os

from task_1 import add_number
from task_2 import gen_psevdonim
from task_3 import create_file
from TASK_04.task_4 import create_file_
from TASK_04.task_5 import create_dif_files
from TASK_04.task_6 import create_dir
from TASK_07.task_7 import group

if __name__ == '__main__':
    add_number(5, 'task01.txt')
    gen_psevdonim('task01.txt')
    create_file('nums.txt', 'psew.txt', 'result.txt')
    create_file_('txt', count_file=3)
    create_dif_files(txt=2, bin=4, png=8)
    create_dir('new')
    group(os.getcwd())
