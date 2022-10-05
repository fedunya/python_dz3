# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def fill_list_random(list_len):
    return [random.randint(1, 9) for i in range(list_len)]
def user_input(a):
    num = input(a)
    while not num.isdigit() or num == '0':
        print('Неверный ввод, повторите!')
        num = input(a)
    num = int(num)
    return num

import os, random
os.system("cls")
list = fill_list_random(user_input('Введите размер списка: '))
print(f'\nЗаданный список -> {list}')
multiply_elem = []
while len(list) > 1:
    multiply_elem.append(list[0]*list[-1])
    del list[0], list[-1] 
if len(list) ==1: multiply_elem.append(list[0]**2)
print(f'\nПроизведение пар чисел списка -> {multiply_elem}\n')
