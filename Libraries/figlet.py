import sys
from pyfiglet import Figlet
import random

def main():

    figlet = Figlet()
    list_of_fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        # not arguments in the command line
        f = random.choice(list_of_fonts)
    elif len(sys.argv) == 3:
        # proper input
        if sys.argv[1] != '-f' and sys.argv[1] != "--font":
            sys.exit("wrong flag")
        if sys.argv[2] not in list_of_fonts:
            sys.exit("Unknown font")

        f = sys.argv[2]

    else:
        sys.exit("too many args")



    figlet.setFont(font=f)


    output_string = input("Input: ")
    print(f"Output: {figlet.renderText(output_string)}")


main()
