print()
new_list = input("Изначальный список: ").lstrip("[").rstrip("]").strip().split(",")
print()


sorted_list = []
for list_item in new_list:
    value = int(list_item)

    pos = 0
    for item in sorted_list:
        pos = sorted_list.index(item)

# Если нашли больше чем вставляемое 
        if item > value:
            break
    else:
# Если нашли меньше чем вставляемое 
        if sorted_list and item < value:
                pos += 1

    
    sorted_list.insert(pos, value)


print()
print(f"Отсортированный список: {sorted_list}")
print()
