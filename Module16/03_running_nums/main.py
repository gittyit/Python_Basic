
shift_amount = int(input("Сдвиг: "))

list_to_shift = input("Изначальный список: ").lstrip("[").rstrip("]").strip().split(",")

shifted_list = []
for list_item in list_to_shift:
    shifted_list.append(int(list_item))

shift_pos = len(shifted_list) - shift_amount
shifted_list_part1 = shifted_list[:shift_pos]
shifted_list_part2 = shifted_list[shift_pos:]

shifted_list = shifted_list_part2 + shifted_list_part1

print(f"Сдвинутый список: {shifted_list}")
