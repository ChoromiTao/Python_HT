# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

def prompt_number(msg):
    a = int(input(msg))
    return a

def summaryize_numbers(number1, number2):
    if number1 == 0:
        return number2
    return summaryize_numbers(number1-1, number2 +1)

number_a = prompt_number("Введите первое число: ")
number_b = prompt_number("Введите второе число: ")
print(summary := summaryize_numbers(number_a, number_b))