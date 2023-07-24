'''
Чтение данных о каталогах
Для получения информации о том какие директории и файлы находятся в текущем каталоге
можно воспользоваться следующими вариантами кода.
'''

import os
from pathlib import Path

print(os.listdir())

p = Path(Path().cwd())
for obj in p.iterdir():
    print(obj)
