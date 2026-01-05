menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}



def main ():
    running_total = 0

    while True:
        try:
            order = input("Item: ").title()
        except EOFError:
            break
        try:
            running_total += menu[order]
        except KeyError:
            continue

        print(f"total: ${running_total:.2f}")

main ()
