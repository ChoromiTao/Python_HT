# Задача *
# Валентина прогуляла лекцию по математике.Преподаватель решил подшутить над нерадивой студенткой и
# попросил ее на практическом занятии перечислить все положительные делители некоторых целых чисел.
# Для несложных примеров студентка быстро нашла решения 
# (для числа 6 это: 1, 2, 3, 6; а для числа 16 это: 1, 2, 4, 8, 16), но этим все не закончилось.
# На домашнее задание ей дали варианты посложнее: 23436, 190187200, 380457890232.

# Решить такое вручную, как вы понимаете, практически нереально.
# Вот Валентина и обратилась к вам за помощью. Помогите ей
# Постарайтесь найти самое оптимальное решение.



number = int(input("Введите это сложное число: "))
dividers = {1}

# for i in range(1, number):
#     if number%i == 0:
#         print(i, end=", ")


for i in range(1,number//2):
    if number%i == 0:
        dividers.add(i)
        dividers.add(number//i)
print(f"Делители числа: ", dividers)


# dividers_2 = ""
# dividers_3 = ""
# dividers_4 = ""
# dividers_5 = ""
# dividers_6 = ""
# dividers_7 = ""
# dividers_8 = ""
# dividers_9 = ""
# dividers_10 = ""
# dividers_others = ""

# if number%2 == 0:
#     print(f"Все делители, кратные 2: ", end=" ")
#     for i in range(2,int(number/2)):
#         if number/(2*i) == 0 and not ((2*i)%4 ==0 or (2*i)%6 == 0 or (2*i)%8 == 0 or (2*i)%10 ==0):
#             dividers_2[i] = 2*i
#             print(dividers_2[i], ", ")
# if number%3 == 0:
#     print(f"\nВсе делители, кратные 3: ", end=" ")
#     for i in range(3,int(number/3)):
#         if number/(3*i) == 0 and not ((3*i)%6 ==0 or (3*i)%9 == 0):
#             dividers_3[i] = 3*i
#             print(dividers_3[i], ", ")
# if number%4 == 0:
#     print(f"\nВсе делители, кратные 4: ", end=" ")
#     for i in range(4,int(number/4)):
#         if number/(4*i) == 0 and not ((4*i)%8 ==0):
#             dividers_4[i] = 4*i
#             print(dividers_4[i], ", ")
# if number%5 == 0:
#     print(f"\nВсе делители, кратные 5: ", end=" ")
#     for i in range(5,int(number/5)):
#         if number/(5*i) == 0 and not ((5*i)%10 ==0):
#             dividers_5[i] = 5*i
#             print(dividers_5[i], ", ")
# if number%6 == 0:
#     print(f"\nВсе делители, кратные 6: ", end=" ")
#     for i in range(6,int(number/6)):
#         if number/(6*i) == 0:
#             dividers_6[i] = 6*i
#             print(dividers_6[i], ", ")
# if number%7 == 0:
#     print(f"\nВсе делители, кратные 7: ", end=" ")
#     for i in range(7,int(number/7)):
#         if number/(7*i) == 0:
#             dividers_7[i] = 7*i
#             print(dividers_7[i], ", ")
# if number%8 == 0:
#     print(f"\nВсе делители, кратные 8: ", end=" ")
#     for i in range(8,int(number/8)):
#         if number/(8*i) == 0:
#             dividers_8[i] = 8*i
#             print(dividers_8[i], ", ")
# if number%9 == 0:
#     print(f"\nВсе делители, кратные 9: ", end=" ")
#     for i in range(9,int(number/9)):
#         if number/(9*i) == 0:
#             dividers_9[i] = 9*i
#             print(dividers_9[i], ", ")
# if number%10 == 0:
#     print(f"\nВсе делители, кратные 10: ", end=" ")
#     for i in range(10,int(number/10)):
#         if number/(10*i) == 0:
#             dividers_10[i] = 10*i
#             print(dividers_10[i], ", ")
# print(f"\nВсе остальные делители: ", end=" ")
# for i in range(11,number):
#     if number%i == 0 and not ():
#           print(6*i, ", ")
