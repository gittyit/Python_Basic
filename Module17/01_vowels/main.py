vowels = ['у','е','ы','а','о','э','я','и','ю','ё']

text_string = input("Введите текст: ")

text_string_vowels = [ _ for _ in text_string if _ in vowels]

print(f"Список гласных букв: {text_string_vowels}")

print(f"Длина списка: {len(text_string_vowels)}")
