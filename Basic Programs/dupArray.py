temp = []

def duplicateArray():
    array = [1,2,23,4,5,5,6,23,5,5,5,5,6,6,54,56,5,5,]

    temp.append(array[0])
    for i in range(2, len(array)):
        flag = False
        for j in range(len(temp)):
            if temp[j] == array[i]:
                flag = False
                break
            else:
                flag = True
        if flag == True:
            temp.append(array[i])


    print(temp)


duplicateArray()
