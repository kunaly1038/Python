import sys

def user_Input():
    userInput = int(input('Enter the Number you want to check is a prime :'))
    return userInput
    
def prime_Check(inputNumber):
    if inputNumber == 1 or inputNumber == 2:
        return True
    elif inputNumber % 2 == 0:
        return False
    else:
        flag = 3
        while flag < inputNumber:
            if inputNumber % flag == 0:
                return False
                break
            flag +=1
        return True


def print_Check(inputNumber, boolValue):
    if boolValue == True:
        print(inputNumber, ' is an PRIME NUMBER')
    elif boolValue == False:
        print(inputNumber, ' is not an PRIME NUMBER')

        
if __name__ == '__main__':
    # while True:
    #     print('Do you want to continue...')
    #     cont = input('Enter Y to continue : ')
    #     if cont == 'y' or cont == 'Y':
    #         userInput = user_Input()
    #         value = prime_Check(userInput)
    #         print_Check(userInput, value)
    #     else:
    #         sys.exit()
    for x in range(1, 2000):
        value = prime_Check(x)
        print_Check(x, value)










        
