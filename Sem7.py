'''У вас есть код, который вы не можете менять (так часто бывает, когда код в 
глубине программы используется множество раз и вы не хотите ничего сломать): 
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный способ вашего взаимодействия с этим кодом - посредством задания 
функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать 
список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values 
получился копией values.
'''
'''trasformation = lambda x: x
values = [1, 23, 42, 'asdfg']
transformed_values = list(map(trasformation, values))
if values == transformed_values:
print('ok')
else:
print('fail')'''

'''Дан список размеров(длина, ширина) эллипсов
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
Напишите функцию find_farthest_orbit(list_of_orbits), которая находит площадь самого большого эллипса и возвращает кортеж с его размерами.
Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b – длины и ширина осей эллипса
- Площадь кругов учитывать не нужно, т.е если у эллипса a == b, то это круг.
При решении задачи используйте списочные выражения.
Гарантируется, что самый большой эллипс всего один.'''
'''# def find_farthest_orbit(list_of_orbits):
# max_s = 0
# for a, b in list_of_orbits:
# s = 3.14 * a * b
# if a != b and s > max_s:
# max_s = s
# result = a, b
# return result

def find_farthest_orbit(list_of_orbits):
list_of_orbits = list(filter(lambda sizes: sizes[0] != sizes[1], list_of_orbits))
list_max_areas = [3.14 * a * b for a, b in list_of_orbits]
max_area = max(list_max_areas)
i_max_area = list_max_areas.index(max_area)
return list_of_orbits[i_max_area]
# return [list_of_orbits[i] for i in range(len(list_of_orbits)) if list_max_areas[i] == max_area][0]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))'''

'''Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение 
некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов 
отличается - то False. Для пустого набора объектов, функция должна возвращать True. 
Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
Ввод:							            Вывод:
values = [0, 2, 10, 6]				        same
if same_by(lambda x: x % 2, values):
	print('same')
else:
	print('different')
'''
'''def same_by(characteristics, objects):
check_0 = characteristics(objects[0])

for num in objects[1:]:
if check_0 != characteristics(num):
return False

return True


values = [3, 1, 1, 7]

if same_by(lambda x: x % 2 == 0, values):
print('same')
else:
print('different')

def same_by_2(characteristics, objects):
res_set = {characteristics(num) for num in objects}
if len(res_set) <= 1:
return True
return False

def same_by_3(characteristics, objects):
result = list(filter(characteristics, objects))
if objects == result or not result:
return True
return False

def same_by_4(characteristics, objects):
result = list(map(characteristics, objects))
if all(result) == any(result):
return True
return False

values = [1, 2, 5, 11]

if same_by_4(lambda x: x % 2 == 0, values):
print('same')
else:
print('different')

'''
import Sem8