print('\nЗадача «Угадай число».\n')

guessed_number = int(input('Загадай число от 1 до 100: '))

num_start = 1
num_end = 100


q_p1 = "Твоё число "
q_p2 = "? (Выберите 1 - равно, 2 - больше, 3 - меньше): "
while True:
    # Cередина отрезка - среднее арифметическое
    ask_num = (num_start + num_end) // 2
    question = q_p1 + str(ask_num) + q_p2
    answer = int(input(question))
    if answer == 1:
        print('Загаданное число:', ask_num)
        break
    elif answer == 2:
        print('число больше')
        num_start = ask_num + 1
    elif answer == 3:
        print('число меньше')
        num_end = ask_num - 1