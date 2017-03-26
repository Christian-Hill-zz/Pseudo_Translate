from dic import *
def wordByWord():
    with open('ADDITION.txt','r') as f:
        for line in f:
            for word in line.split():
                print(word)
wordByWord()
