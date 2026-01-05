import sys


def main ():

    valid_arg(sys.argv)
    counter = 0
    with open(sys.argv[1]) as file:
        for line in file:
            if line.strip() == "" or line.strip().startswith("#"):
                continue
            else:
                counter += 1

    print(counter)


def valid_arg(argv):
    # length check
    if len(argv) > 2:
        sys.exit("Too many command-line args")
    elif len(argv) < 2:
        sys.exit("Too few command-line args")
    
    # checking for python file
    if argv[1].endswith("py"):
        print(argv[1][-3:])
        sys.exit("Not a python file")

    try:
        with open(argv[1]) as file:
            pass
    except FileNotFoundError:
        print(argv[1][-3:])
        sys.exit("Does not exist here")

    return True


if __name__ == "__main__":
    main()
