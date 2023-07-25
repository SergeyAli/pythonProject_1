'''
Задание №3
✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
✔ При достижении конца более короткого файла, возвращайтесь в его начало.
'''

def create_file(file_nums: str, file_psew: str, file_res: str):
    with (
        open(file_nums, 'r', encoding='utf-8') as f_nums,
        open(file_psew, 'r', encoding='utf-8') as f_psew,
        open(file_res, 'w', encoding='utf-8') as f_res
    ):
        f_psew_len = len(f_psew.readlines())
        f_nums_len = len(f_nums.readlines())

        for i in range(0, max(f_nums_len, f_psew_len)):
            spam = f_nums.readline().strip()
            eggs = f_psew.readline().strip()
            if not spam:
                f_nums.seek(0)
                spam = f_nums.readline().strip()
            if not eggs:
                f_psew.seek(0)
                eggs = f_psew.readline().strip()

            curr_list = spam.split('|')
            mult = int(curr_list[0]) * float(curr_list[1])

            f_res.write(f'{eggs.lower()} {abs(mult)}\n' if mult < 0 else f'{eggs.upper()} {round(mult)}\n')



if __name__ == '__main__':
    create_file('nums.txt', 'psew.txt', 'result.txt')

