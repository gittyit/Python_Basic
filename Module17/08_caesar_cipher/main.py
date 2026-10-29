

def encrypt_message(message):
    encrypted_message = ""
    for char in message:
        if alphabet.count(char) > 0:
            char_pos = alphabet.index(char)
            new_pos = char_pos + shift 
            if new_pos >= 32:
                new_pos = shift - (32 - char_pos) - 1
            new_char = alphabet[new_pos]
            encrypted_message += new_char
        else:
            encrypted_message += char
    return encrypted_message


alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к",
            "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц",
            "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]

message = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))

encrypted_message = encrypt_message(message)
print(f"Зашифрованное сообщение: {encrypted_message}")
