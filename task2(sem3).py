# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

N = int(input('Введите N: '))
min = int(input('Введите min: '))
max = int(input('Введите max: '))
result_list = []
my_list = []

for i in range(N):
    my_list.append(randint(min, max))
print(my_list)

for i in range((len(my_list)+1)//2):
    result_list.append(my_list[i]*my_list[len(my_list)-1-i])
print(result_list)