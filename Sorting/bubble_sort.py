def bubble_sort():
    #Enter the size of the array for to definde the size of the array
    array=[]
    x = int(input('How many Elements you want in Array :'))
    #this is for inseting the elements into the array
    for i in range(x):
        y = int(input('Enter the element :'))
        array.append(y)
    #here the bubble sort is being applied using two for loops
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j+1]<array[j]:
                array[j], array[j+1] = array[j+1], array[j]
    print(array)

bubble_sort()
