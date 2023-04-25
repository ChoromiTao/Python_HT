# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

from random import randint

def prompt(msg):
    a = int(input(msg))
    return a

def maximal_bushes_harvest(garden_bushes):
    max_summary = 3*len(garden_bushes)
    for i in range(len(garden_bushes)):
            if (garden_bed[i-2] + garden_bed[i-1] + garden_bed[i]) > max_summary:
                max_summary = garden_bed[i-2] + garden_bed[i-1] + garden_bed[i]
    return max_summary

bushes, bushes_harvest_min, bushes_harvest_max = prompt("Сколько будет кустов на грядке?: "), prompt("Минимальное количество ягод с куста?: "), prompt("Максимальное количество ягод с куста?: ")
garden_bed = [randint(bushes_harvest_min, bushes_harvest_max) for i in range(bushes)]
print(garden_bed)
max_summary = maximal_bushes_harvest(garden_bed)
print(f"Максимальное количество ягод при единоразовом сборе получится {max_summary} ягод с трёх кустов")