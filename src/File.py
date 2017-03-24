from dic import *
def wordByWord():
    test=[]
    with open('ADDITION.txt','r') as f:
        for line in f:
            for word in line.split():
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
