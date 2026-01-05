def main():
    current_due = 50

    while current_due > 0:
        print(f"Amount due: {current_due}")
        current_inserted = int(input("Insert coins: "))

        if current_inserted in {25, 10, 5}:
            current_due -= current_inserted 
        
    print(f"Change Owed: {abs(current_due)}")


main()
