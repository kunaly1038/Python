def arrayDuplicate():
    array = [1,2,2,2,3,4,5,5,5,5,5,5,5,5,5,5,5,5,5,6,6,54,56]
    temp = []
    j = 0
    for i in range(len(array)-1):
        if array[i] != array[i+1]:
            temp.append(array[i])
    print(temp)

arrayDuplicate()
