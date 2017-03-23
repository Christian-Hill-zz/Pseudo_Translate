from dic import *
def wordByWord():
    with open('ADDITION.txt','r') as f:
        for line in f:
            for word in line.split():
                print(word)
def Array():
    with open("ADDITION.txt", "r") as ins:
        array = []
        for line in ins:
            array.append(line)
        print (array)
wordByWord()
Array()
