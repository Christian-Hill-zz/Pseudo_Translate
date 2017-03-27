from dic import *
def wordByWord():
    test=[]
    with open('ADDITION.txt','r') as f:
        for line in f:
            for word in line.split():
<<<<<<< HEAD
                print(word)
wordByWord()
=======
                test.append(word)
                #print(word)
                #print(test)
        return (test)
def Array():
    with open("ADDITION.txt", "r") as ins:
        array = []
        for line in ins:
            array.append(line)
        print (array)

net=wordByWord()
Array()
print net
>>>>>>> 6e8e4b940e883506e3550af34c6325ceae1590b4
