shop = [
        ['каретка', 1200],
        ['шатун', 1000],
        ['седло', 300],
        ['педаль', 100],
        ['седло', 1500],
        ['рама', 12000],
        ['обод', 2000],
        ['шатун', 200],
        ['седло', 2700]
]


item = input("Название детали: ")

quantity = 0
total_amount = 0

for shop_index in shop:
    if item == shop_index[0]:
        quantity += 1
        total_amount += shop_index[1]

print(f"Кол-во деталей —  — {quantity}")
print(f"Общая стоимость — {total_amount}")
