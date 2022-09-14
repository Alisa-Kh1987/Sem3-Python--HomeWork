#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# Первый способ
# num = int(input('Укажите число в десятичной системе счисления: '))
# print(f'{num:b}')


#Второй способ
num = int(input('Укажите число в десятичной системе счисления: ')) 
num_bin = ''
 
while num > 0:
    num_bin = str(num % 2) + num_bin
    num = num // 2
 
print(num_bin)