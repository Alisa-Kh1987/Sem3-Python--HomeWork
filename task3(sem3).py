# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.
# Пример:# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

n = int(input('Укажите размер списка: '))
min = int(input('Введите минимальное значение диапазона: '))
max = int(input('Введите максимальное значение диапазона: '))
my_list = []

for i in range(n):
    my_list.append(random.uniform(min, max))
    my_list=[round(i,3) for i in my_list]
print(my_list)

max_fract = my_list[0]%1
min_fract = my_list[0]%1
for i in range(1,len(my_list)):
    if my_list[i]%1>max_fract:
        max_fract = round(my_list[i]%1, 3)
    if my_list[i]%1<min_fract:
        min_fract = round(my_list[i]%1, 3)
print(f'Максимальное значение дробной части: {max_fract}')
print(f'Минимальное значение дробной части: {min_fract}')
print(f'Разность между максимальным и минимальным значением дробной части: {round(max_fract - min_fract, 3)}')