odd_money = 0

def get_odd_money(order):
    cash = order[0]
    price = order[1]
    return cash % price


def get_food(order):
    cash = order[0]
    price = order[1]
    return cash // price

def get_order():
    print("К вам подошел оффициант и спросил заказ")
    cash = int(input("Вы ему дали 1 купюру номиналом = "))
    price = float(input("Цена одного блюда = "))
    return [cash, price]


order1 = get_order()
odd_money += get_odd_money(order1)
print("Он вам принес", str(int(get_food(order1))) + "порций")

order2 = get_order()
odd_money += get_odd_money(order2)
print("Он вам принес", str(int(get_food(order2))) + "порций")

order3 = get_order()
odd_money += get_odd_money(order3)
print("Он вам принес", str(int(get_food(order3))) + "порций")

print("Общая сдача осталась у официанта в сумме", str(round(float(odd_money), 2)) + "долларов")


