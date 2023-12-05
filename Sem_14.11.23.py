"""
Задача №9.  По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
Input:       5
Output:    120
_________________________________________________________
a = input("Input a number: ")
while not a.isdigit() or a == "0":
    print("Error input")
    a = input("Input a number: ")

x = int(x)
fact = 1
num = 1
while num <= x:
    fact, num = fact * num, num + 1
print(fact)

2

a = i5act)
"""

# ___________________________________________________________
"""
Задача №11. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
Input:     21
Output:  9
Ряд чисел Фибоначчи:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711,
"""

"""
a = input("Input a number: ")

while not a.isdigit() or a == "0" or a == "1":
    print("Error input")
    a = input("Input a number: ")

a = int(a)

pos = 3
pred = 1
pred2 = 1
while pred < a:
    pred, pred2 = pred + pred2, pred
    pos += 1

if pred != a:
    print(-1)
else:
    print(pos)

#2
pos = 3
pred = 1
pred2 = 1
while pred < a:
    temp = pred
    pred = pred + pred2
    pred2 = temp
    pos += 1
"""

# ____________________________________________________________________
"""
Пользователь вводит число N (1 ≤ N ≤ 10). Далее построчно N чисел от -50 до 50. Нужно вывести наибольшее количество идущих подряд положительных чисел.
Input:    6 -> -20 30 -40 50 10 -10
Output: 2

import random

days_num = int(input("Введите кол-во дней: "))

max_thaw_days = 0
thaw_days = 0
for i in range(days_num):
    # temperature = random.randint(-50, 50)
    temperature = int(input("Введите температуру: "))
    # print(temperature, end=" ")
    if temperature > 0:
        thaw_days += 1
    else:
        if thaw_days > max_thaw_days:
            max_thaw_days = thaw_days
        thaw_days = 0

if thaw_days > max_thaw_days:
    max_thaw_days = thaw_days

print(f'{max_thaw_days = }')
print(f'{2+3*5**2 = }')
"""

# 2

"""days_num = int(input("Введите кол-во дней: "))

max_thaw_days = 0
thaw_days = 0
for i in range(days_num):
    # temperature = random.randint(-50, 50)
    temperature = int(input("Введите температуру: "))
    # print(temperature, end=" ")
    if temperature > 0:
        thaw_days += 1
        if thaw_days > max_thaw_days:
            max_thaw_days = thaw_days
    else:
        thaw_days = 0


print(f'{max_thaw_days = }')
"""

# ________________________________________________
"""Задача №15. 1) Иван Васильевич пришел на рынок и решил
купить два арбуза: один для себя, а другой для тещи. Понятно,
что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
Но вот незадача: арбузов слишком много и он не знает как же
выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество арбузов.
Вторая строка содержит N чисел, записанных на новой
строчке каждое. Здесь каждое число – это масса
соответствующего арбуза
2) Пользователь вводит одно число N.  Далее идут N чисел,
записанных на новой строчке каждое. Вывести максимальное и
минимальное (циклы)
Input:	5 -> 5 1 6 5 9
"""

"""num = int(input("Enter a number: "))

min_weight = 1000
max_weight = 0

for _ in range(num):
    weight = int(input("Enter a number: "))

    if weight > max_weight:
        max_weight = weight

    if weight < min_weight:
        min_weight = weight

print(max_weight, min_weight)
"""
# 2

"""from random import randint

num = randint(1, 20)
weight = randint(5, 15)
print(weight, end=" ")
min_weight = weight
max_weight = weight

for _ in range(num - 1):
    weight = randint(5, 15)
    print(weight, end=" ")

    max_weight = max(max_weight, weight)
    min_weight = min(min_weight, weight)

print()
print(max_weight, min_weight)
"""
