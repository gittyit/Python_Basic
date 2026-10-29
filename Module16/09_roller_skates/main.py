

def create_skates_list(number_of_skates):
    roller_skate_size_list = []
    skates_index = 1
    while skates_index <= number_of_skates:
        roller_skate_size = input(f"Размер {skates_index}-ой пары: ")
        roller_skate_size_list.append(roller_skate_size)
        skates_index += 1
    return roller_skate_size_list


def get_total_people_for_skating(number_of_people):
    total_people_for_skating = 0
    man_index = 1
    while man_index <= number_of_people:
        man_feet_size = input(f"Размер ноги {man_index}-го человека: ")
        man_feet_size_list.append(man_feet_size)
        
        if roller_skate_size_list.count(man_feet_size):
            total_people_for_skating += 1
            roller_skate_size_list.remove(man_feet_size)
        
        man_index += 1
    return total_people_for_skating


output_line = "Наибольшее кол-во людей, которые могут взять ролики"

man_feet_size_list = []

number_of_skates = int(input("Кол-во коньков: "))
roller_skate_size_list = create_skates_list(number_of_skates)

print()
number_of_people = int(input("Кол-во людей: "))

total_people_for_skating = get_total_people_for_skating(number_of_people)

print()
print(f"{output_line}: {total_people_for_skating}")
