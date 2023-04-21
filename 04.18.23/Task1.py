# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint

def fill_list(dimention):
    my_list = [randint(0,10) for i in range(0, dimention)]
    return my_list

def prompt(msg):
    number = int(input(msg))
    return number

def uniq_sorted_list(list1, list2):
    list1, list2 = set(list1), set(list2)
    set_both = set()
    for item in list1:
        for jtem in list2:
            if item == jtem:
                set_both.add(item)
    set_both = list(set_both)
    set_both.sort()
    return set_both

list_number_one = fill_list(prompt("Введите размерность первого набора чисел: "))
list_number_two = fill_list(prompt("Введите размерность второго набора чисел: "))
print(f"{list_number_one}\n{list_number_two}")
list_both = uniq_sorted_list(list_number_one, list_number_two)
print(list_both)