words = input("Введите фразы через пробел: ").split()
vowels = ('a', 'e', 'i', 'o', 'u', 'y')
result = []

for word in words:
    word_vowels = tuple(filter(lambda x: x in vowels, word))
    result.append(word_vowels)

print(result)