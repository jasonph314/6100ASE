def main():

    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    
    while True:
        date = input("Date: ")
        parts = date.split('/')

        if len(parts) == 3:

            try:
                month = int((parts[0]))
                day = int((parts[1]))
                year = int((parts[2]))

                if month < 1 or month > 12 or day < 1 or day > 31:
                    continue

                break
            except ValueError:
                continue

        else:
            # months + words, not just numbers
            try:
                parts = parts[0].split(' ')
                month = int(months.index(parts[0])) + 1
                day = int(parts[1].replace(',', ''))
                year = int(parts[2])

                if day < 1 or day > 31:
                    continue

                break

            except ValueError:
                continue

    print(f"{year}-{month:02}-{day:02}")



main()
