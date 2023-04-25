# *****Напишите функцию , которая будет возвращать переданное в качестве параметра n число словами

# Input -> 435467
# Output -> четыреста тридцать пять тысяч четыреста шестьдесят семь

# ЕСТЬ ИДЕЯ ЧЕРЕЗ РЕКУРСИЮ, ПОСМОТРИ ТЕСТИНГ
# МОЖЕТ СДЕЛАТЬ ФУНКЦИЮ РЕКУРСИИ И ОТДЕЛЬНО ФУНКЦИЮ ПРОВЕРКИ СЛОВАРЕЙ??

dictionary_units = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
dictionary_in_dozen = {10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать', 
                       16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}
dictionary_dozens = {20: 'двадцать', 30: 'тридцать', 40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят', 80: 'восемьдесят', 
                     90: 'девяносто'}
dictionary_hundreds = {1: 'сто', 2: 'двести', 3: 'триста', 4: 'четыреста', 5: 'пятьсот', 6: 'шестьсот', 7: 'семьсот', 
                       8: 'восемьсот', 9: 'девятьсот'}
dictionary_units_for_thousands = {1: 'одна', 2: 'две', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
dictionary_thousands_in_units = {'тысяча': '1', 'тысячи': '2' '3' '4', 'тысяч': '5' '6' '7' '8' '9'}
dictionary_millions_in_units = {'миллион': '1', 'миллиона': '2' '3' '4', 'миллионов': '5' '6' '7' '8' '9'}
dictionary_billions_in_units = {'миллиард': '1', 'триллиона': '2' '3' '4', 'триллионов': '5' '6' '7' '8' '9'}
dictionary_billions_in_units = {'триллион': '1', 'триллиона': '2' '3' '4', 'триллионов': '5' '6' '7' '8' '9'}

def prompt(msg):
    a = int(input(msg))
    return a

def naming_number(number, temp = 0):
    if number // 1_000_000_000_000 >= 1:
        return print("Я сама не вышепчу этого числа, напиши другое)))")
    else:
        if number // 100_000_000_000 < 10:
            temp = number//100_000_000_000
            for key in dictionary_hundreds.keys():
                if temp == key:
                    print(dictionary_hundreds.values(key), end=" ")
            temp = (number// 10_000_000_000)%10
            if temp <10:
                for key in dictionary_units.keys():
                    if temp == key:
                        print(dictionary_units.values(key), end=" ")
            elif 10 <= temp <20:
                for key in dictionary_in_dozen.keys():
                    if temp == key:
                        print(dictionary_in_dozen.values(key), end=" ")
            elif temp >= 20:
                for key in dictionary_dozens.keys():
                    if temp == key:
                        print(dictionary_dozens.values(key), end=" ")

current_number = prompt("Введите число: ")