def charCount():
    char2 = input('Enter the string : ')
    char = char2.split()
    y = {}
    for x in char:
        if x in y:
            y[x] +=1
        else:
            y[x] = 1
    print(y)
charCount()
