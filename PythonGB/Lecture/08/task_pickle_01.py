'''
3. Pickle
Python предлагает модуль pickle для сериализации и десериализации своих структур в поток байт.
Преобразования возможны в любом месте и в любое время, если вы используете Python. Но данные окажутся бесполезными,
если вы передаёте их для обработки другим ЯП.
'''

import pickle
import os

res = pickle.loads(b"cos\nsystem\n(S'echo Hello world!'\ntR.")
print(f'{res= }')

os.system('echo Hellp world!')
