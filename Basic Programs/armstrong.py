num = int(input('Enter the Number : '))
arm = 0
while(num>0):
    temp = num % 10
    temp = temp * temp * temp
    arm += temp
    num = num //10


print(arm)

