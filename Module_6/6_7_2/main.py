num = int(input("Введите число:"))
digits = 0
while num != 0:
    digits += 1
    num = num // 10
print("Кол-во цифр в числе:", digits)