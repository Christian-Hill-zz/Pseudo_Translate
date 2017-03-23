from dic import *


def main():
    with open("ADDITION.txt", "r") as ins:
        array = []
        for line in ins:
            array.append(line)
    print(array)


main()

