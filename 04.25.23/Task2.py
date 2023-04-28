# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

# Диапазон от 6 до 12

# Вывод: [1, 9, 13, 14, 19]

from random import randint

def prompt(msg):
    a = int(input(msg))
    return a

def prompt_range(msg):
    a = [int(input(msg)), int(input())]
    return a

def list_key(length = prompt("Введите длину списка: "), new_diapazone = prompt_range("Введите диапазон для поиска индексов: "), list_index = []):
    new_list = [randint(0,20) for i in range(length)]
    print(new_list)
    for i in range(length):
        if new_list[i] in range(new_diapazone[0], new_diapazone[1]+1):
            list_index.append(i)
    return list_index

print(list_index :=list_key())