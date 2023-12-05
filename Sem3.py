#  Задача №17. Дан список чисел. Определите, сколько в нем встречается 
#  различных чисел.

#  Input: [1, 1, 2, 0, -1, 3, 4, 4]

#  Output: 6

# Примечание: Пользователь может вводить значения списка или список задан 
#  изначально.

# from random import randint

# num_list = []

# list_length = randint(5, 10)
# print(f'{list_length=}')

# for _ in range(list_length):
#     new_num = randint(0, 5)
#     num_list.append(new_num)
#     print(num_list)


# num_list_2 = [randint(0, 5) for _ in range(list_length)]


# print(num_list_2)

# unique = set(num_list_2)
# print(unique)
# print(f'{len(unique)=}')

from random import randint

# list_length = randint(5, 10)
# print(f'{list_length=}')



# num_list_2 = [randint(0, 5) for _ in range(list_length)]
# print(f'{num_list_2=}')

# new_list = []

# for num in num_list_2:
#     if num not in new_list:
#         new_list.append(num)
# print(f'{new_list=}')

# print(f'{len(new_list)=}')


# for num in num_list_2:
#     if num in new_list:
#         continue
#     new_list.append(num)

# ________________________________________________________

# Задача №19.  Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K 
# элементов вправо,  K – положительное число.

# Input:   [1, 2, 3, 4, 5] k = 3

# Output:  [3, 4, 5, 1, 2]

# Примечание: Пользователь может вводить значения списка или список задан 
# изначально.

# [1, 2, 3, 4, 5] k = 2
# [4, 5, 1, 2, 3]

# [1, 2, 3, 4, 5, 6, 7, 8] k = 4
# [5, 6, 7, 8, 1, 2, 3, 4]
# k = 4
# new_list = [randint(0, 5) for _ in range(randint(5, 10))]
# print(new_list)
# # res_list = new_list[-k:] + new_list[:-k]
# # print(res_list)

# for shift in range(k):
#     shifter_num = new_list.pop()
#     new_list.insert(0, shifter_num)
# print(new_list)

# ____________________________________________________________________
# Задача №21. Напишите программу для печати всех уникальных значений в словаре. 

# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
#          {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}] 

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


# Примечание: Список словарей задан изначально. Пользователь его не вводит

# list_dicts = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# my_set = set()

# for curr_dict in list_dicts:
#     for val in curr_dict.values():
#         my_set.add(val.strip())
# print(my_set)

# ________________________________________________________________
# Задача №23. Дан массив, состоящий из целых чисел. Напишите программу, 
# которая подсчитает количество элементов массива, больших предыдущего 
# (элемента с предыдущим номером) 
# Input: [0, -1, 5, 2, 3]
# Output: 2 
# Пояснение: (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения списка или список 
# задан изначально.

data_list = [0, -1, 5, 2, 3]
count = 0

for i in range(len(data_list)-1):
    if data_list[i] < data_list[i+1]:
        count+=1
print(f'{count=}')

new_list = [1 for i in range(len(data_list)-1) if data_list[i] < data_list[i+1]]
print(sum(new_list))

new_list = [1 for i in range(len(data_list)-1) if data_list[i] < data_list[i+1] else 0]
print(sum(new_list))







# if letter.isascii() and letter.isalpha():
#     print('строка состоит из английских букв')

# ________________________________________________
my_dict = {'Иванов':1, 'Петров': 2, 'Сидоров':3, 'Николаев':4}
# print(f'{my_dict=}')
# print(f'{my_dict["Петров"]=}')
# print()
# print(f'{len(my_dict.keys())=}')
# print(f'{sum(my_dict.values())=}')
# print(f'{my_dict.items()=}')
# print()
# print(f'{list(my_dict.keys())[3]=}')
# print(f'{list(my_dict.values())=}')
# print(f'{list(my_dict.items())=}')
# print()

# for key in my_dict:
#     print(key, end='\t')
# print('\n')

# for key in my_dict.keys():
#     print(key, end='\t')
# print('\n')

# for value in my_dict.values():
#     print(value, end='\t')
# print('\n')

# for item in my_dict.items():
#     print(item, end='\t')
# print('\n')

# q,w,*e = (111,222)
# print(q)
# print(w)
# print(e)

# my_list = [(1,2,3), (11,22,33), (111,222,333)]
# for q,w,*e in my_list:
#     print(q, w, e, sep='-')
    
for key, value in my_dict.items():    
    print(key,value, sep=': ', end='\t')
print('\n')