
number_of_people = int(input("Кол-во человек: "))
number_to_quit = int(input("Какое число в считалке? "))

print(f"Значит, выбывает каждый {number_to_quit}-й человек")

list_of_people = list(range(1, number_of_people + 1))

index_to_start = 0
index = 0

while number_of_people > 1:
    index += 1
    
    number_to_start = list_of_people[index_to_start]

    print()
    print(f"Текущий круг людей: {list_of_people}")
    print(f"Начало счёта с номера {number_to_start}")

    list_of_people_len = len(list_of_people)

    number_to_remove = number_to_quit

    ind = index_to_start
    number_to_quit_left = number_to_quit
    while True:
        if ind == list_of_people_len - 1:
            ind = 0
        else:
            ind += 1

        number_to_quit_left -= 1

        if number_to_quit_left == 1:
            break
    
    index_to_remove = ind
    # Start is next after removed
    index_to_start = ind

    number_to_remove = list_of_people[index_to_remove]

    list_of_people.pop(index_to_remove)

    # Start is first if last removed
    if ( index_to_remove == (list_of_people_len - 1) ):
        index_to_start = 0
    
    number_of_people -= 1
    
    print(f"Выбывает человек под номером {number_to_remove}")

print()
print(f"Остался человек под номером {list_of_people[0]}")
