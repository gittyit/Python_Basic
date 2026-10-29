a = int(input("Введите число 1: "))
b = int(input("Введите число 2: "))
c = int(input("Введите число 3: "))

if a > b and a > c:
    max = a
    num = "первое"
elif b > a and b > c:
    max = b
    num = "второе"
elif c > a and c > b:
    max = c
    num = "третье"

print("Максимальное число: ", max, ", (", num, ').', sep='')