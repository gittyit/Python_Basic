cards_count = int(input("Введите количество карточек: "))
cards_sum = 0

for i in range(1, cards_count + 1):
    cards_sum += i

for i in range(1, cards_count):
    cards_sum -= int(input("Введите номер оставшейся карточки: "))

print(f"Номер пропавшей карточки: {cards_sum}")