import sys
import csv
from tabulate import tabulate


def main():

    valid_arg(sys.argv)
    with open(sys.argv[1]) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(tabulate(reader, headers="keys", tablefmt="grid"))








def valid_arg(argv):
    n = len(argv)
    if n < 2:
        sys.exit("No arguments")
    elif n > 2:
        sys.exit("Too many args")

    try:
        with open(argv[1]) as file:
            pass
    except FileNotFoundError:
        sys.exit("Does not exist")
    
    ## function concludes - we're this is valid
















if __name__ == "__main__":
    main()
