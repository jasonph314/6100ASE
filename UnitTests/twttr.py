def main():
    word = input("Word: ")


def shorten(word):
    output_string = ""
    for char in word:
        if char.upper() in {'A', 'E', 'I', 'O', 'U'}:
            continue
        
        output_string += char

    return output_string


 
if __name__ == "__main__":
    main()
