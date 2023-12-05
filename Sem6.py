'''Задача №39. 
Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, 
в каком они идут в первом массиве), которых нет во втором массиве. Пользователь вводит  
число N - количество элементов в первом массиве, затем N чисел - элементы массива. 
Затем число M - количество элементов во втором массиве. Затем элементы второго массива
Ввод: 					Вывод:
7					    3 3 2 12
3 1 3 4 2 4 12
6
4 15 43 1 15 1
'''
'''
from random import randint


def get_array(size):
    # res = []
    # for _ in range(size):
    #     res.append(randint(0,5))


    return [randint(0,5) for _ in range(size)]

    
def arr_diff(array1, array2):
    # res = []
    # for num in array1:
    #     if num not in array2:
    #         res.append(num)
    return [num for num in array1 if num not in array2]

    # return [num if num not in array2 else 0  for num in array1 ]
    

size_1 = int(input('Введите размер первого массива: '))
size_2 = int(input('Введите размер второго массива: '))

arr_1 = get_array(size_1)
print(f'{arr_1=})
arr_2 = get_array(size_2)
print(f'{arr_2=})

res_arr = arr_diff(arr_1, arr_2)
print(*res_arr)
'''



'''Задача №41. 
Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве 
выведет количество элементов, у которых два соседних и, при этом, оба соседних 
элемента меньше данного. Сначала вводится число N — количество элементов в массиве  
Далее записаны N чисел — элементы массива. Массив состоит из целых чисел. 

Ввод: 			Ввод:
5			        5
1 2 3 4 5			1 5 1 5 1

Вывод:			Вывод:
0				    2
'''
'''
from random import randint

size_arr_new = int(input('Введите размер массива: '))

arr_new = [randint(0, 5) for _ in range(size_arr_new)]

print(arr_new)

count = 0

for i in range(1, len(arr_new)-1):
    if arr_new[i-1]<arr_new[i]>arr_new[i+1]:
        count+=1
print(count)
#var2
print(sum([1 for i in range(1, len(arr_new)-1) if arr_new[i-1]<arr_new[i]>arr_new[i+1]]))

'''



'''Задача №43.
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, 
что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
Вводится список чисел. Все числа списка находятся на разных строках.
Ввод:			Вывод:
1 2 3 2 3			2
'''
'''
arr_size = int(input('Введите размер массива: '))
arr_new = [randint(0, 5) for _ in range(arr_size)]
print(arr_new)

#1
count = 0
for i in range(arr_size - 1):
    for j in range(i + 1, arr_size):
        if arr_new[i] == arr_new[j]:
count += 1

print(count)


#2
count = 0
for num in set(arr_new):
    count_num = arr_new.count(num)
    count += count_num * (count_num - 1) // 2

print(count)
'''



'''Задача №45.
Два различных натуральных числа n и m называются дружественными, если сумма делителей 
числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – 
дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое 
из которых не превосходит k. Программа получает на вход одно натуральное число k, не 
превосходящее 105. Программа должна вывести  все пары дружественных чисел, каждое из 
которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. 
Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
Ввод:			Вывод:
300			220 284
'''

def get_sum_div(num):
    sum_div = 1
    for div in range(2, num):
        if num % div == 0:
            sum_div += div
    return sum_div


def chec_friend_num(number):
    for first_num in range(2, number):
        second_num = get_sum_div(first_num)
        if get_sum_div(second_num) == first_num and first_num < second_num:
            print(first_num, second_num)


k = int(input("Введите число: "))
chec_friend_num(k)