'''
Задание №6
Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки)
и число (номер попытки, с которой она угадана).
Функция формирует словарь с информацией о результатах отгадывания.
Для хранения используйте защищённый словарь уровня модуля.
Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
Для формирования результатов используйте генераторное выражение.
'''


from task_4 import game_02

_dict_log = dict()


def multy_game():
    dict_all = {'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],
                'Не лает, не кусает, в дом не пускает': ['замок'],
                'Сидит дед во сто шуб одет': ['лук', 'луковица']}

    for question, answers in dict_all.items():
        res = game_02(question, answers)
        add_dict_log(question, res)


def add_dict_log(quesestion: str, answer: int):
    _dict_log[quesestion] = answer

def print_result():
    result = (f'Загадка: {key} - результат - {"Не угадали" if value == 0 else f"Угадалди с {value} попытки"}' for key, value
              in _dict_log.items())

    print('\n'.join(result))


if __name__ == '__main__':
    multy_game()
    print_result()
