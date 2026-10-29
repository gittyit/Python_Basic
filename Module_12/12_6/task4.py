def count_letters(text, digit, character):
    digit_count = 0
    char_count = 0

    for text_char in text:
        if text_char == digit:
            digit_count += 1
        if text_char == character:
            char_count += 1
    
    print(f"Количество цифр {digit}: {digit_count}")
    print(f"Количество букв {character}: {char_count}")



text = input("Введите текст: ")
digit = input("Какую цифру ищем? ")
character = input("Какую букву ищем? ")
print()
count_letters(text, digit, character)