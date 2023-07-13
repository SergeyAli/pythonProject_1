# Задание №2
# Погружение в Python | Коллекции
# Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях
def task_2():
    current_txt: str = input('введите строку: \n')

    if current_txt.isdigit():
        return  int(current_txt)
    elif current_txt.replace('.', '', 1).isdigit():
        return float(current_txt)
    elif current_txt[0] == '-' and current_txt.replace('-', '', 1).replace('.', '', 1).isdigit():
        return float(current_txt)
    elif current_txt.lower() != current_txt:
        return current_txt.lower()
    else:
        return current_txt.upper()

print(task_2())
