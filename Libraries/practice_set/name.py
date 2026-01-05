import sys

#sys.argv - argument vector - list



if len(sys.argv) < 2:
    sys.exit("too few")

for arg in sys.argv[1:-1]:
    # Print name tags
    print("hello, my name is", arg) # no argument gives index error






