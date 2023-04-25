# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def prompt(msg):
    a = int(input(msg))
    return a

def arith_progression():
    arith_progrssn = list()
    first_el, diff_progrssn, length = prompt("Введите первый элемент прогрессии: "), prompt("Введите разницу прогрессии: "), prompt("Длина прогрессии?: ")
    arith_progrssn.append(first_el)
    for i in range(1, length):
        next_el = arith_progrssn[0] + i*diff_progrssn
        arith_progrssn.append(next_el)
        print(f"Элемент {i}: {next_el}")
    return arith_progrssn

arithmetic_progression = arith_progression()
