# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

print("Дети делали журавлики...")
s = int(input("Сколько журавликов сделали дети?: "))

if s%6 != 0:
    print("А ещё один журавлик сделали Вы? Может дети сделали не столько?")
else:
    print(f"Петя сделал {int(s/6)} журавликов, и Серёжа тоже {int(s/6)}. А Катя молодец, сделала {int(2*s/3)} журавликов, Катя пирожок возьмёт")