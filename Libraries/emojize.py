import emoji

def main ():

    input_string = input("Input: ")
    print(f"Output: {emoji.emojize(input_string, language='alias')}")
    




main()
