#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

# def Fibonacci(n):
#     if n in [1, 2]:                       
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)

# def NegaFibonacci(n):
#     if n == 1:                       
#         return 1
#     elif n == 2:                       
#         return -1
#     else:
#         num1, num2 = 1, -1
#         for i in range(2, n):
#             num1, num2 = num2, num1 - num2
#         return num2

# my_list = [0]
# k = int(input('Введите число: '))
# for i in range(1, k + 1):
#     my_list.append(Fibonacci(i))
#     my_list.insert(0, NegaFibonacci(i))
# print(my_list)