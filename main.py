menu = {
    "кава еспресо": {
        "number": 1,
        "price": 25,
    },
    "кава американо": {
        "number": 2,
        "price": 30,
    },
    "кава латте": {
        "number": 3,
        "price": 35,
    },
    "кава мокко": {
        "number": 4,
        "price": 40,
    },
    "кава раф": {
        "number": 5,
        "price": 38,
    },
    "кава Ірлантська": {
        "number": 5,
        "price": 44,
    },
}


def print_menu():
    for item, info in menu.items():
        print(f"{info['number']}. {item}: {info['price']} грн")


def process_order():
    order = {}
    while True:
        item = input("Введіть номер кави (або '=' для завершення): ")
        if item == "=":
            break

        if item not in menu:
            print("Неіснуючий номер кави.")
            continue

        quantity = int(input("Введіть кількість: "))
        order[item] = quantity
    return order


def calculate_total(order):
    total = 0
    for item, quantity in order.items():
        total += menu[item]["price"] * quantity
    return total


def calculate_change(total, payment):
    return payment - total


def print_receipt(order, total, payment, change):
    print("=== Квитанція ===")
    for item, quantity in order.items():
        info = menu[item]
        print(f"{info['number']}. {item}: {quantity} x {info['price']} грн = {info['price'] * quantity} грн")
    print(f"Загальна вартість: {total} грн")
    print(f"Отримано: {payment} грн")
    print(f"Решта: {change} грн")


while True:
    print_menu()
    order = process_order()
    total = calculate_total(order)
    payment = int(input("Введіть суму оплати: "))
    change = calculate_change(total, payment)
    print_receipt(order, total, payment, change)

    again = input("Бажаєте зробити ще одне замовлення? (y/n): ")
    if again.lower() != "y":
        break

print("Дякуємо за покупку!")