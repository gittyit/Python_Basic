def digits_operation(number, operation):
    if operation == "min":
        result = 9
    else:
        result = 0
    
    while number != 0:
        digit = number % 10
        number = number // 10
        if operation == "sum":
            result += digit
        elif operation == "max":
            if result < digit:
                result = digit
        elif operation == "min":
            if result > digit:
                result = digit
    return result

def digits_sum(num):
  result_sum = digits_operation(num, "sum")
  print(f"Сумма цифр: {result_sum}")

def digits_max(num):
  result_max = digits_operation(num, "max")
  print(f"Максимальная цифра: {result_max}")

def digits_min(num):
  result_min = digits_operation(num, "min")
  print(f"Минимальная цифра: {result_min}")


def main_menu():
    number = int(input("Введите число: "))
    print("Введите номер действия:")
    print("1 - сумма цифр")
    print("2 - максимальная цифра")
    action = int(input("3 - минимальная цифра: "))
    if action == 1:
        digits_sum(number)
    elif action == 2:
        digits_max(number)
    elif action == 3:
        digits_min(number)

while True:
    main_menu()