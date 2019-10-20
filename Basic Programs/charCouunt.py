def charCount():
    char = input('Enter the string : ')
    y = {}
    for x in char:
        if x in y:
            y[x] +=1
        else:
            y[x] = 1
    print(y)
charCount()
