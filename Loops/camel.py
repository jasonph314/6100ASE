    
def main():
   print(to_snake(get_input()))

def get_input():
    userInput = str(input("camelCase: "))
    return userInput

def to_snake(userInput):
    snake_output = ""
    for char in userInput:
        if char.isupper():
            snake_output += '_'
            snake_output += char.lower()
        else:
            snake_output += char

    return snake_output



main()
