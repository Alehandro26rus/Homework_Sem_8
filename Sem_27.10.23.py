# Задача №1.  За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут длиной m километров? При решении
# этой задачи нельзя пользоваться условной конструкцией if и циклами.
# Input:
# n = 700км/д
# s= 750км
# Output:
# 2

# import this
import math
import os


# n = int(input("Введите скорость автомобиля : "))
# m = int(input("Введите необходимое расстоние : "))

# # print(math.ceil(m/n))
# print((m + n-1)//n)

# скорость - 700
# расстояние хотя бы на 1 больше скорости,
# 1 день - 1 до 700
# 2 день - 701 до 1400
# 3 день - 1401 до 2100

# n-1 = 700 - 1 = 699 //700 = 1
# если m = 701 то  701 +699 = 1400 //700 = 2
# если m = 1400 то 1400 +699 = 2099 // 700 = 2
# если m = 750 то  750 +699 = 1449 // 700 = 2
# print((m + n-1)//n)
#  (n-1)//n =0

os.system("cls")

# n = int(input("Введите скорость авто: "))
# m = int(input("Введите необходимое расстояние: "))

# print(-(-m // n))
# print(math.ceil(m / n))
# print(m // n + (m % n > 0))
# print((m + n-1) // n)

# _____________________________________________________________
# В некоторой школе решили набрать три новых математических класса
# и оборудовать кабинеты для них новыми партами. За каждой партой может
# сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# x = int(input("Qty of student in 1.class: "))
# y = int(input("Qty of student in 2.class: "))
# z = int(input("Qty of student in 1.class: "))

# # print(f'It is required to buy {(-(-x//2)-(-y//2)-(-z//2))} scool desks')
# print(f'It is required to buy {((x+1)//2+(y+1)//2+(z+1)//2)} scool desks')
# _______________________________________________________________________

# Вагоны в электричке пронумерованы натуральными числами, начиная с 1
# (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с
#  «хвоста»; это зависит от того, в какую сторону едет электричка).
# В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда
# и обнаружил, что его вагон имеет номер j. Он хочет определить, сколько всего
# вагонов в электричке. Напишите программу, которая будет это делать или
# сообщать, что без дополнительной информации это сделать невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

# a = int(input('В какой вагон сел? '))
# b = int(input('Какой номер вагона? '))
# if a == b:
#     print('Невозможно посчитать вагоны')
# else:
#     print('Всего вагонов ', ((a+b)//2)*2)
# _______________________________________________________________________________

# Дано натуральное число. Требуется определить, является
# ли год с данным номером високосным. Если год является високосным,
# то выведите YES, иначе выведите NO.
# Напомним, что в соответствии с григорианским календарем, год
# является високосным, если его номер кратен 4, но не кратен 100,
# а также если он кратен 400.
# Input: 2000
# Output: YES

year = int(input("Input the year to check: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("YEAS")
else:
    print('NO')
# _______________________________________________________

# n = 24
# x = n / 6
# y = (2/3) * n
# print(int(x), int(y), int(x))
# задача из дз
# ____________________________________________________________
text = input('введите что-нибудь')
# print(int(input('введите что-нибудь: ')))

# print(float(text))
print(bool(text))

n = 5
n = bool([])
print(int(n))

# ____________________________________
a = 'Python'
b = 'Hello world!'
v = '\nПривет\n, меня зовут Вася, \nмне 28 лет!\n'
# my_sep = '-||-'
# print(a,b,v)
# print(a,b,v, sep=my_sep , end='\n')
print(a, end=v)
print(b, end=v)
print(v)
# print()
print(*'Python', sep='\n') # -> print('P', 'y', 't', 'h', 'o', 'n')
print(*['P','y','t','h','o','n'], sep='~') # -> print('P', 'y', 't', 'h', 'o', 'n')

# ____________________________________________________
name = "John"
print('Hi, %s.' % name)  #- Hi, John
print('Hi, {name}'.format(name=name)) # - Hi, {name}
print(f'Hi, {name}.')#  - Hi, John.
x = 2+5 * 90 // 12 **23
print(2+5 * 90 // 12 **23)
print(f'{2+5 * 90 // 12 **23}')
print(f'{2+5 * 90 // 12 **23 = }')
print(f'{x = }')