'''
Задание №3
✔ Продолжаем развивать задачу 2.
✔ Возьмите словарь, который вы получили. Сохраните его итераторатор.
✔ Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.
'''

def task_2():
    my_str = input('ведите строку: \n')
    my_dict: dict = {s: ord(s) for s in my_str}
    return my_dict


def task_3():
    my_dict_s = task_2()

    spam = iter(my_dict_s.items())
    for i in range(0, 5):
        print(next(spam))

task_3()