num = int(input('Enter the number : '))
num2 = 0
temp =0

while(num> 0):
    num2 = num % 10
    temp = temp+num2
    num = num//10

print(temp)
