# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Введите, до какого числа будете искать степени двойки: "))
i = 1

while 2**i <= n:
    print(2**i, end=", ")
    i+=1