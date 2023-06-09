# ***Чтобы лучше разобраться в типах параметров функций Инна создала inspect_function(), 
# которая в качестве аргумента принимает другую функцию (главное, не встроенную, built-in).
# В результате работы она выводит следующие данные: название анализируемой функции, 
# наименование всех принимаемых ею параметров и их типы (позиционные, ключевые и т.п.).
# Попробуйте повторить результат девушки.

# В данном случае на подмогу приходит модуль inspect. С его помощью можно реализовать задуманный функционал.

# Пример:

# def my_func(a, b, /, c, d, *args, e, f, **kwargs):
# pass

# Анализируем функцию my_func
# a: POSITIONAL_ONLY
# b: POSITIONAL_ONLY
# c: POSITIONAL_OR_KEYWORD
# d: POSITIONAL_OR_KEYWORD
# args: VAR_POSITIONAL
# e: KEYWORD_ONLY
# f: KEYWORD_ONLY

# kwargs: VAR_KEYWORD
# Анализируем функцию sqrt
# x: POSITIONAL_ONLY

