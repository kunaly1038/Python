def insertion_sort():
    #Enter the size of the array for to definde the size of the array
    array=[]
    x = int(input('How many Elements you want in Array :'))
    #this is for inseting the elements into the array
    for i in range(x):
        y = int(input('Enter the element :'))
        array.append(y)
    #here the insertion sort is being applied using two for loops
    for i in range(x):
        key = array[i] #the value of i index is being inserted into the key variable
        j = i-1        
        while(j >= 0 and key < array[j]):#here the value before the ith index is being checked weather it is smaal from the jth index element
              array[j+1] = array[j]
              j-=1
        array[j+1]=key
    print(array)

insertion_sort()
