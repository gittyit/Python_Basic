
numbers_list = []

numbers_count = int(input("Количество чисел: "))


for index in range(numbers_count):
    number = int(input("Число: "))
    numbers_list.append(number)

numbers_to_add = []
numbers_list_len = len(numbers_list)

pos_to_get = numbers_list_len - 2

if numbers_list[numbers_list_len-1] == numbers_list[numbers_list_len-2]:
    pos_to_get -= 1

for index in range(pos_to_get, -1, -1):
    number_to_add = numbers_list[index]
    numbers_to_add.append(number_to_add)

numbers_to_add_len = len(numbers_to_add)


print(f"Последовательность: {numbers_list}")
print(f"Нужно приписать чисел: {numbers_to_add_len}")
print(f"Сами числа: {numbers_to_add}")
