

def  largest_smallest_number(number1, number2):
        if number1 > number2:
            largest_number = number1
            smallest_number = number2
        else:
            largest_number = number2
            smallest_number = number1

        # print(f"наибольшее число={largest_number}")
        # print(f"наименьшее число={smallest_number}")
        # print()

        return largest_number, smallest_number


def euclidean_gcd_algorithm(number1, number2):
    numbers_greatest_common_divisor = 0

    # наибольшое и наименьшее число
    largest_number, smallest_number = largest_smallest_number(number1, number2)

    # алгоритм Евклида
    divisable = largest_number
    divisor = smallest_number
    remainder = 1
    while True:
        print(f"делимое={divisable} делитель={divisor}")

        integer_part = divisable // divisor
        remainder = divisable % divisor

        # print(f"целая часть от деления={integer_part}")
        print(f"остаток от деления={remainder}")
        print()

        if remainder == 0:
            numbers_greatest_common_divisor = divisor
            break

        divisable = divisor
        divisor = remainder

    return numbers_greatest_common_divisor


def regular_gcd_algorithm(number1, number2):
    numbers_greatest_common_divisor = 0

    # наибольшое и наименьшее число
    largest_number, smallest_number = largest_smallest_number(number1, number2)
    
    for divisor in range(1, largest_number):
        if (largest_number % divisor == 0 and
            smallest_number % divisor == 0 and
            divisor > numbers_greatest_common_divisor):
            numbers_greatest_common_divisor = divisor
            print(f"делитель {divisor}")
    return numbers_greatest_common_divisor


number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
print()

# numbers_greatest_common_divisor = regular_gcd_algorithm(number1, number2)
numbers_greatest_common_divisor = euclidean_gcd_algorithm(number1, number2)

print(f"Наибольший общий делитель: {numbers_greatest_common_divisor}")