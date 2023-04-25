def numbertowords(n):
    ones = "", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"
    teens = "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"
    tens = "", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"
    thousands = "", "тысяча", "тысячи", "тысяч"
    
    if n < 10:
        return ones(n)
    elif n < 20:
        return teens(n-10)
    elif n < 100:
        return tens(n//10) + (" " + ones(n%10) if n%10 != 0 else "")
    elif n < 1000:
        return ones(n//100) + " hundred" + (" and " + numbertowords(n%100) if n%100 != 0 else "")
    else:
        for i in range(3, 0, -1):
            if n // (10(3*i)) > 0:
                return numbertowords(n//(10(3*i))) + " " + thousands(i) + (" " + numbertowords(n%(10(3*i))) if n%(10(3*i)) != 0 else "")
        return numbertowords(n//1000) + " " + thousands(3) + (" " + numbertowords(n%1000) if n%1000 != 0 else "")