'''
Запись и добавление в файл
● Запись методом write
Метод write принимает на вход строку или набор байт в зависимости от того как вы открыли файл.
После записи метод возвращает количество записанной информации.
'''

text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'
with open('new_data.txt', 'a', encoding='utf-8') as f:
    res = f.write(text)
    print(f'{res = }\n{len(text) = }')
