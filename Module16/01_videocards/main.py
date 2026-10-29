
old_videocards_model_list = []

videocards_count = int(input("Количество видеокарт: "))

videocards_number = 0
while videocards_number < videocards_count:
    videocards_number += 1
    videocard_model = int(input(f"Видеокарта {videocards_number}: "))
    old_videocards_model_list.append(videocard_model)

new_videocards_model_list = list(old_videocards_model_list)

biggest_videocards_model = list(new_videocards_model_list)
biggest_videocards_model.sort(reverse=True)
biggest_videocards_model = biggest_videocards_model[0]

for videocard_index in new_videocards_model_list:
    if videocard_index == biggest_videocards_model:
        new_videocards_model_list.remove(videocard_index)

old_videocards_model_list = str(old_videocards_model_list).replace(",", "")
new_videocards_model_list = str(new_videocards_model_list).replace(",", "")

print()
print(f"Старый список видеокарт: {old_videocards_model_list}")
print()
print(f"Новый список видеокарт: {new_videocards_model_list}")
