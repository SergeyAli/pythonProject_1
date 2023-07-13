# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

stuff = {'Спальник': 5, 'Палатка': 10,'Спички': 1, 'Сухой паек': 3, 'Стакан': 2}

def backpack_capacity(capacity: int, stuff: dict) -> list[str]:
    packaging_option = []
    for key, value in stuff.items():
        if value <= capacity:
            capacity -= value
            packaging_option.append(key)
    return packaging_option

print(backpack_capacity(20, stuff))
