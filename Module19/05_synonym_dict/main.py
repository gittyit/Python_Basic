
def get_pair_number(number):
    number_text = ""
    if number == 0:
        number_text = "Первая"
    elif number == 1:
        number_text = "Вторая"
    elif number == 2:
        number_text = "Третья"
    elif number == 3:
        number_text = "Четвертая"
    elif number == 4:
        number_text = "Пятая"
    elif number == 5:
        number_text = "Шестая"
    elif number == 6:
        number_text = "Седьмая"
    elif number == 7:
        number_text = "Восьмая"
    elif number == 8:
        number_text = "Девятая"
    elif number == 9:
        number_text = "Десятая"
    return number_text


def get_synonym(word, synonyms):
    word = word.casefold()
    res = [print(f"Синоним: {synonyms[item] if item.casefold() == word else item}") for item in synonyms.keys() if item.casefold() == word or synonyms[item].casefold() == word]

    if res == []:
        print("Такого слова в словаре нет.")


pairs_number = int(input("Введите количество пар слов: "))

synonyms = {}

for line_index in range(pairs_number):
    line = input(f"{get_pair_number(line_index)} пара: ")
    if line.count("-") > 0:
        delimeter = "-"
    elif line.count("—") > 0:
        delimeter = "—"
    else:
        print("пары разделяются с помощью тире")
        exit()

    pairs = line.replace(" ", "").split(delimeter)
    synonyms.update({pairs[0]:pairs[1]})



print()

for _ in range(2):
    word = input("Введите слово: ")
    get_synonym(word, synonyms)

