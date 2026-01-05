def main():

    output_string = value(input("Greeting: "))
    print(f"${output_string}")


def value(greeting):

    user_input = greeting.lower()
    n = len(user_input)
    if n != 0:
        if user_input == "hello":
            return 0
        elif user_input[0] == "h":
            return 20

    return 100

if __name__ == "__main__":
    main()

