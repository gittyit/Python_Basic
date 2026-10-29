
list_len = int(input("Введите длину списка: "))

result_list = [1 if _ % 2 == 0 else _ % 5 for _ in range(0, list_len)]

print(f"Результат: {result_list}")
