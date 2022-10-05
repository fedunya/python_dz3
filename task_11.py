# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def fill_list_random(list_len):
    list = [random.randint(1, 9) for i in range(list_len)]
    return list
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
print(f'\nСумма элементов списка на нечетных позициях -> {sum(list[::2])}\n')
