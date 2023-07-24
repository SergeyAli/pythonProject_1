'''
Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
'''

line_path = r'C:\Games\Dishonored 2\Dishonored2.exe'


def split_path(abs_path: str) -> tuple():
    list_abs_path = abs_path.split('\\')
    list_last_elem = list_abs_path[-1].split('.')
    path = '\\'.join(list_abs_path[0:-1])
    name = list_last_elem[0]
    expansion = list_last_elem[1]
    print(f'Путь: {path}\nИмя файла: {path}\nРасширение файла: {expansion}')
    return path, name, expansion


split_path(line_path)


