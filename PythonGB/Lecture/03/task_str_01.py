# Строки, str
# Работа со строками как с массивами
# Начнём с квадратных скобок

text = 'Hello world!'
print(text[6])
print(text[3:7])

# Если необходимо заменить элемент новым, индексы не подойдут. Для этих целей нужен метод replace

new_txt = text.replace('l', 'L', 2)
print(text, new_txt, sep='\n')