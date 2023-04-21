# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def prompt_number(msg):
    a = int(input(msg))
    return a

def exponentional(number1, number2):
    if number2 == 1:
        return number1
    return number1 * exponentional(number1, number2-1)

base_number = prompt_number("Введите возводимое в степень число: ")
exponent_number = prompt_number("Введите степень для числа: ")
print(expo := exponentional(base_number, exponent_number))