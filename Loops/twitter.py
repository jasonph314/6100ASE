def main():

    input_string = input("Input: ")

    output_string = ""
    for char in input_string:
        
        if char.upper() in {'A', 'E', 'I', 'O', 'U'}:
            continue
        else:
            output_string += char

    print(output_string)


main()
