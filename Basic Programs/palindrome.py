num = int(input('Enter the Number : '))
palin = 0

while num > 0:
    temp = num % 10
    palin *=10
    palin = palin + temp
    num = num // 10

print(palin)
