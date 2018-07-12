def selection_sort():
    #Enter the size of the array for to definde the size of the array
    array=[]
    x = int(input('How many Elements you want in Array :'))
    #this is for inseting the elements into the array
    for i in range(x):
        y = int(input('Enter the element :'))
        array.append(y)
    #here the insertion sort is being applied using two for loops
    for i in range(len(array)):
        min = i
        for j in range(i+1,len(array)):
            if array[min]>array[j]:
                min = j
        array[min], array[i]= array[i], array[min]
    print(array)

selection_sort()
-
