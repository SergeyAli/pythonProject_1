'''
● Метод seek
Метод seek позволяет изменить положение “курсора” в файле. seek(offset, whence=0),
где offset — смещение относительно опорной точки, whence - способ выбора опороной точки.
● whence = 0 - отсчёт от начала файла
● whence = 1 - отсчёт от текущей позиции в файле
● whence = 2 - отсчёт от конца файла
Метод возвращает новую позицию “курсора”.
'''

last = before = 0
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
    print(f'{last = }, {before = }')
    print(f'{f.seek(before, 0) = }')
    f.write('\n'.join(text))
