# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# from multiprocessing.sharedctypes import Value
# from random import randint

# N = int(input('Введите N: '))
# min = int(input('Введите min: '))
# max = int(input('Введите max: '))
# summ_nums = 0
# my_list = []

# for i in range(N):
#     my_list.append(randint(min, max))
# print(my_list)

# for index in range(len(my_list)):
#     if index%2==1:
#         summ_nums+=my_list[index]
# print(summ_nums)