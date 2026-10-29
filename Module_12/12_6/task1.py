def summa_n(num):
  summ = 0
  for num in range(1, num + 1):
    summ += num
  return summ

number = abs(int(input("Введите число: ")))
result = summa_n(number)
print(f"Сумма чисел от 1 до {number} равна {result}")