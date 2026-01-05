from random import randrange

def main():
    level = get_level()
    score = 0

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        counter = 0

        while counter < 3:
            try:
                answer = int(input(f"{x} + {y} = ")) ## big mistake - you forgot to typecast to int + a typo
            except ValueError:
                print("EEE")
                counter += 1
                continue
            
            if answer == x + y:
                score += 1
                break
            else:
                counter += 1
                print("EEE")
                continue
        if counter == 3:
            print(f"{x} + {y} = {x+y}")

    print(f"Score: {score}/10")




def get_level():

    while True:
        try:
            level = int(input("Level: "))
        except ValueError: # if user enters bad value
            continue
        if level not in {1, 2, 3}:
            continue
        
        return level



def generate_integer(level):

    if level not in {1,2,3}:
        raise ValueError
    
    if level == 1:
        start = 0
        end = 10**level
    else:
        start = 10**(level-1)
        end = 10**level

    
    return randrange(start, end)


if __name__ == "__main__":
    main()
