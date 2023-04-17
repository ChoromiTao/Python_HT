dictionary_english = {1: 'A' 'E' 'I' 'O' 'U' 'L' 'N' 'S' 'T' 'R',
                      2: 'D' 'G',
                      3: 'B' 'C' 'M' 'P',
                      4: 'F' 'H' 'V' 'W' 'Y',
                      5: 'K',
                      8: 'J' 'X',
                      10: 'Q' 'Z'
                      }

dictionary_russian = {1: 'А' 'В' 'Е' 'И' 'Н' 'О' 'Р' 'С' 'Т',
                      2: 'Д' 'К' 'Л' 'М' 'П' 'У',
                      3: 'Б' 'Г' 'Ё' 'Ь' 'Я',
                      4: 'Й' 'Ы',
                      5: 'Ж' 'З' 'Х' 'Ц' 'Ч',
                      8: 'Ш' 'Э' 'Ю',
                      10: 'Ф' 'Щ' 'Ъ'
                      }

word = input("Введите искомое слово/Input seeking world: ").upper()
summary_letters, count = 0, 0

while count != 2:
    correct_word = True
    while correct_word:
        count = 0
        for item in word:
            for points, letters in dictionary_english.items():
                if item in letters:
                    summary_letters += points
                    if count == 0:
                        count += 1
                        break
            for points, letters in dictionary_russian.items():
                if item in letters:
                    summary_letters += points
                    if count == 1:
                        count += 1
                        print("Напишите слово правильно!Wriht the word corretly!")
                        break
        if len(word) < 2:
            print("Слово слишком короткое/Word is too short")
            break

print(f"Количество очков слова/Total point is: {summary_letters}")