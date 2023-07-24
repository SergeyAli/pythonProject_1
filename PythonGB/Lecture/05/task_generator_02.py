# Генераторные выражения
# Генераторные выражения Python позволяют создать собственный генератор, перебирающий значения.

my_gen = (chr(i) for i in range(97, 123))
print(my_gen) # <generator object <genexpr> at 0x000001ED58DD7D60>
for char in my_gen:
    print(char)