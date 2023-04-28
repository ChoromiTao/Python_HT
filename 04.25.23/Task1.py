# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def prompt(msg):
    a = int(input(msg))
    return a

def arith_progression(arith_progrssn = list()):
    first_el, diff_progrssn, length = prompt("Введите первый элемент прогрессии: "), prompt("Введите разницу прогрессии: "), prompt("Длина прогрессии?: ")
    for i in range(length):
        arith_progrssn.append(next_el := first_el + i*diff_progrssn)
        print(f"Элемент {i+1}: {next_el}")
    return arith_progrssn

arithmetic_progression = arith_progression()
