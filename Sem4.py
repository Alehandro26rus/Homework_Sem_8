''' Задача №25. Напишите программу, которая принимает на вход строку, и 
отслеживает, сколько раз каждый символ уже встречался. Количество повторов 
добавляется к символам с помощью постфикса формата _n.

Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

Для решения данной задачи используйте функцию .split()
'''

'''#1
input_data = 'a a a b c a a d c d d'
input_list = input_data.split()

output = ''
count_dict = {}
for letter in input_list:
    output += letter
    if letter in count_dict:
        count_dict[letter] += 1
        output += f'_{count_dict[letter]}'
    else:
        count_dict[letter] = 0
        output += ' '   

print('a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2')
print(output)

#2

input_data = 'a a a b c a a d c d d'
input_list = input_data.split()

count_dict = {}
for letter in input_list:
    print(f'{letter}{count_dict.get(letter, "")}', end=' ')
    number_letter = count_dict.get(letter, 0) + 1
    count_dict[letter] = number_letter


print()
print('a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2')  
'''

'''Задача №27. Пользователь вводит текст(строка). Словом считается последовательность 
непробельных символов идущих подряд, слова разделены одним или большим числом пробелов. 
Определите, сколько различных слов содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells that she sells are sea shells 
       I'm sure So if she sells sea shells on the sea shore I'm sure that the shells 
       are sea shore shells
'''

'''text_string = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"

text1 = text_string.lower().split()
print(len(set(text1)))

'''

'''Задача – «На вход программе подаются натуральные числа,как только пользователь введёт 0 
ввод прекращается. Вывести наибольший элемент получившейся последовательности».
Есть два кода с ошибками, нужно определить где ошибок меньше.

# Ваня:

n = int(input())
max_number = n #1 max_number = 1000
while n != 0:
    n = int(input())
    if max_number < n: #2 max_number > n
        max_number = n
print(max_number)


# Петя:

# n = int(input())
# max_number = -1
# while n > 0: #1 while n < 0:
#   if max_number < n:
#       max_number = n #2 n = max_number
#       n = int(input()) #3 перенесли ввод данных за if
# print(max_number) #4 print(n)

'''





