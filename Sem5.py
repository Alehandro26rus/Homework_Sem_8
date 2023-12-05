''' Задача №31. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 13

Задание необходимо решать через рекурсию

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711
'''
'''
def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

num = int(input('Введите число: '))
print(fib(num))
'''




'''Задача №33. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4

Output: 1 3 3 3 1
'''
'''# from random import randint
import time
n = randint(5,15)
list1 = [randint(1,5) for _ in range(n)]
print(list1)

start_time = time.time()
min_num = min(list1)
max_num = max(list1)

for i in range(len(list1)):
if list1[i] == max_num:
list1[i] = min_num
print(list1)

end_time = time.time()
print(end_time - start_time)

#2 variant
from random import randint
import time

n = randint(5,15)
list1 = [randint(1,5) for _ in range(n)]
print(list1)

start_time = time.time()

min_num = list1[0]
max_num = list1[0]
list_max_num = [0]

for i in range(1, len(list1)):
if list1[i] > max_num:
max_num = list1[i]
list_max_num = [i]
elif list1[i] == max_num:
list_max_num.append(i)
if list1[i]<min_num:
min_num=list1[i]

for i in list_max_num:
list1[i]=min_num

print(list1)

end_time = time.time()
print(end_time - start_time)
'''




'''Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
'''
'''
def simple_num(number):
for div in range(2, number):
if number % div == 0:
return False
return True

def num_check(number):
if number.isdigit() and int(number) > 1:
return True
return False

num = input('Enter a number: ')

while not num_check(num):
print('Incorrect number!')
num = input('Enter a number: ')

num = int(num)
print('YES' if simple_num(num) else 'NO')

#2 variant

def simple_num(number):
if number % 2 == 0 or number % 3 == 0 and number not in (2,3):
return False
for div in range(3, int(number ** 0.5) + 1, 2):
if number % div == 0:
return False
return True

def num_check(number):
if number.isdigit() and int(number) > 1:
return True
return False

num = input('Enter a number: ')

while not num_check(num):
print('Incorrect number!')
num = input('Enter a number: ')

num = int(num)
print('YES' if simple_num(num) else 'NO')
'''




'''Задача 37. Дано натуральное число N и последовательность из N  элементов. Требуется вывести эту последовательность в обратном порядке. 
Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
'''
'''
def reverse(num):
if num == 0:
return ''
k = input("Введите число: ")
return reverse(num-1) +' '+ k

n = int(input("Введите кол-во эл-тов: "))

print(reverse(n))

#2 variant

from random import randint

def reverse(num):
if num == 1:
return str(randint(0, 100))
k = str(randint(0, 100))
print(k)
return reverse(num - 1) + ' ' + k

n = int(input('Enter a number of elements: '))
print(reverse(n))
'''


