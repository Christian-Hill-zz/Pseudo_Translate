fp = open('ADDITION.txt')
with open("ADDITION.txt", "r") as ins:
    while 1:
        line = fp.readline()
        if not line:
            pass
        else:
            print line
            array = []
            array.append(line)
            print(array)
