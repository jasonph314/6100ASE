


def main ():
    item_list = dict()
    while True:
        try:
            item = input("Item: ").upper()
        except EOFError:
            print()
            break

        item_list[item] = item_list.get(item, 0) + 1


    for key in sorted(item_list):
        print(f"{item_list[key]} {key}")





























main ()
