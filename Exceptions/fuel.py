def main ():

    while True:
        value = input("Fraction: ")
        parts = value.split('/')
            

        try:
            x = int(parts[0])
            y = int(parts[1])
            if x > y:
                continue
            output = x/y
            break

        except ValueError:
            continue

        except IndexError:
            continue
        except ZeroDivisionError:
            continue

    if output > .99:
        print('F')
    elif output < .01:
        print('E')
    else:
        output = output * 100
        print(f"{output:.1f}%")






main()

