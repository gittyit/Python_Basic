goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

result = []

for item in goods:
    item_id = goods[item]
    sum_amount = 0
    item_stock_quantity = 0

    # Get item stock amount
    for item_stock in store[item_id]:
        item_stock_quantity += item_stock.get("quantity", 0)
        sum_amount += item_stock["quantity"] * item_stock["price"]
    
    result.append([item, item_stock_quantity, sum_amount])


{print(f"{item[0]} — {item[1]} штук, стоимость {item[2]} рубля") for item in result}

