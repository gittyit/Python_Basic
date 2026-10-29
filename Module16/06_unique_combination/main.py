

def sort_list(list1):
    sorted_list = []

    for list_item in list1:
        value = int(list_item)

        pos = 0
        for item in sorted_list:
            pos = sorted_list.index(item)

    # Если нашли больше чем вставляемое
            if item > value:
                sorted_list.insert(pos, value)
                break
    # Если нашли дубликат
            elif item == value:
                break
        else:
    # Есть отсортированные значения
            if sorted_list:
    # Если нашли меньше чем вставляемое
                if item < value:
                    pos += 1
                    sorted_list.insert(pos, value)
    # Список еще не создан
            else:
                sorted_list.insert(pos, value)

    return sorted_list


def merge_sorted_lists(list1: list, list2: list):
    list1.extend(list2)
    sorted_list = sort_list(list1)
    return sorted_list


# Пример использования:
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(merged)
