# Параметры args и kwargs
# Отдельно разберём пару особых параметров. Звёдочка args и две звёздочки kwargs.
# Важно! Python в первую очередь смотрит на звёздочки, а не на имя переменной. Но среди разработчиков приняты имена args и kwargs.
# Они делают код привычным, т.е. повышают читаемость. Не используйте другие переменные.
# Начнём с *args:
def mean(args):
    return sum(args) / len(args)

print(mean([1, 2, 3]))
print(mean(1, 2, 3)) # TypeError: mean() takes 1 positional argument but 3 were given

