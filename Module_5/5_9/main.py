# Почтовое отделение:
# 1. Открывается в 08:00 и закрывается в 22:00.
# 2. С 14:00 до 15:00 - обед. (не выдаёт поссылки)
# 3. C 10:00 и 18:00 разгрузка посылок. (не выдаёт поссылки)

def check_hour():
    print('\nЗадача «Почта».\n')

    question = "Введите время получения поссылки (чч) от 0 до 23, ('q' - выход): "
    str1 = input(question)
    if str1 == 'q':
        return False
    hour = int(str1)

    answer = 'Посылку получить нельзя.'
    if hour >= 8 and hour < 22:
        if ( (hour >= 8 and hour < 10) or
            (hour >= 18) ):
            answer = 'Можно получить посылку.'

    print(answer)
    return True

if  __name__ == '__main__':
    check_hour()