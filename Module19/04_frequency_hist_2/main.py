

def get_frequency(text_line):
    # Create dictionary of chars and their frequency in text line
    # Layout: { char : count(char) }
    return { char:text_line.count(char) for char in text_line }

def get_list_of_keys(frequency, value, keys):
    # Create list of keys for value
    return [ key for key in keys if frequency[key] == value ]

def get_inverted_frequency(frequency):
    keys = list(frequency.keys())

    # Layout: { value : [ keys ] }
    return {value: get_list_of_keys(frequency, value, keys) for value in frequency.values()}


text_line = input("Введите текст: ")

frequency = get_frequency(text_line)

print("Оригинальный словарь частот:")

[print(f"{item} : {frequency[item]}") for item in frequency]

inverted_frequency = get_inverted_frequency(frequency)

print()
print("Инвертированный словарь частот:")

[print(f"{item} : {inverted_frequency[item]}") for item in inverted_frequency]