words = input("Введите фразы через пробел: ").split()
vowels = ('a', 'e', 'i', 'o', 'u', 'y')
result = []

for word in words:
    word_vowels = tuple(filter(lambda x: x in vowels, word))
    result.append(word_vowels)

print(result)


dict_vowels = {1: "а" "е" "ё" "и" "о" "у" "ы" "э" "ю" "я", 2: "-"}
dict_delimiter = {"stop": " "}
sum_vowels, count = list(), 0

def prompt(msg):
    return poetry:= list(input(msg)) 

def reading(poetry, poetry_new: list()):
    poetry_new = [letter for letter in poetry if letter in dict_vowels.values()]
    for letter in poetry:
        if letter in dict_delimiter.values(" "):
            count +=1
    while j < count:
        sub_poetry = list()
        if letter in poetry_new in dict_vowels.values() and not dict_delimiter.values():
            sub_poetry.append(letter)
            #if #короче допилить стоп на пробел и очистку подсторчки. И куда сохранять результат???