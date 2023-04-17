# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

# Задача 18: Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

maxx = length = int(input("Введите длину списка: "))
minn, near_number, temp, temp_min = 1, maxx + 1, 0, maxx

list_number = [random.randint(minn, maxx) for i in range(length)]
print(list_number)
frequency_number = int(input("\nВведите число, частоту которого хотите определить: "))
count = 0

for number in list_number:
    if number == frequency_number:
        count +=1
if count > 0:
    print(f"Число {frequency_number} встречается {count} раз")
else:
    for number in list_number:
        temp = abs(number - frequency_number)
        if temp < temp_min:
            temp_min = temp
            near_number = number
    print(f"Ближайшее число к искомому: {near_number}")
    for number in list_number:
        if number == near_number:
            count +=1
    if count > 0:
        print(f"И тогда ближайшее число {near_number} встречается {count} раз")
