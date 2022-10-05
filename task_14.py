# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def user_input(a):
    num = input(a)
    while not num.isdigit():
        print('Неверный ввод, повторите!')
        num = input(a)
    num = int(num)
    return num

import os
os.system("cls")
decimal_num = user_input('Введите целое число: ')
binary_num = ''
if decimal_num == 0: binary_num = '00000'
while decimal_num > 0:
    binary_num = str(decimal_num % 2) + binary_num
    decimal_num = decimal_num // 2
print(f'\nДвоичное представление числа -> {binary_num}\n')
