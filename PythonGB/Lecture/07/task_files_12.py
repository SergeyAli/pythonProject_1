'''
Чтение методом readline
Для чтения текстового файла построчно используют метод readline.
'''

with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.readline():
        print(res)
