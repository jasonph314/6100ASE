def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    n = len(s)
    if n > 6 or n < 2:
        return False
    else:
        if not s[0:2].isalpha() or not s.isalnum():
            return False

    seen_digit = False
    first_digit_valid = False
    for char in s:
        if not seen_digit and char.isdigit():
            seen_digit = True
            if char != '0':
                first_digit_valid = True
            else:
                return False
        if seen_digit and char.isalpha():
            return False
    return True



if __name__ == "__main__":
    main()
