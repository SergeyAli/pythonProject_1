# Классы bytes и bytearray
# Уделим несколько строк лекции неизменяемым байтам и их изменяемой версии —
# массиву байт. Для отправки информации по каналам связи объекты не подойдут.
# Даже текст не отправить. А вот пересылать байты — легко.

text_en = 'Hello world!'
res = text_en.encode('utf-8')
print(res, type(res))
text_ru = 'Привет, мир!'
res = text_ru.encode('utf-8')
print(res, type(res))