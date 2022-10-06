# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def user_input(a): # функция пользовательского ввода
    num = input(a)
    while not num.isdigit():
        print('Неверный ввод, повторите!')
        num = input(a)
    num = int(num)
    return num
def fib(n): # функция вычисления числа Фибоначчи
    if n == 0: return 0
    elif n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

import os
os.system("cls")
k = user_input('Введите целое число: ')
fibonacci = []
for i in range(0, k+1): # заполнение списка числами Фибоначчи
    fibonacci.append(fib(i))
for i in range(1, k+1): # заполнение списка числами негафибоначчи
    fibonacci.insert(0, (-1)**(i+1) * fib(i))
print(f'\nЧисла Фибоначчи и негафибоначчи для k = {k}:\n{fibonacci}\n')
