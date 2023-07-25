'''
● Чтение CSV
Функция csv.reader принимает на вход файловый дескриптор и построчно читает информацию.
'''

import csv

with open('biostats.csv', 'r', newline='') as f:
    csv_file = csv.reader(f)
    for line in csv_file:
        print(line)

print(type(line))
