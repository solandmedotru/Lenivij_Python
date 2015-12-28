def how_much(price, money):
    return int(money) // int(price)

my_money = input("Введите количество денег = ")
item_price = input("Введите стоимость товара = ")
print("Вы можете купить", str(how_much(item_price, my_money)) + " штук")
