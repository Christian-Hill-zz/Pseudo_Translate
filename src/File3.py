from dic import *
def main():
    with open("ADDITION.txt", "r") as ins:
        with open('ADDITION.txt','r') as f:
                for line in f:
                    for word in line.split():
                        with open("ADDITION.txt", "r") as ins:
                            array = []
                            for line in ins:
                                array.append(line)
                                print (array)
                                print(word)
                                array = []
                                for line in ins:
                                    array.append(line)
                            print(array)
main()
