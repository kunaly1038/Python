def user_Input():
    return int(input('Enter the number till you want prime number'))


def check_prime(userInput):
    for flag in range(userInput):
        if(return_value(flag)):
            print(flag)


def return_value(flag):
    if flag == 1 or flag == 2:
        return True
    elif flag % 2 == 0:
        return False
    else:
        count = 3
        while count < flag:
            if flag % count == 0:
                return False
                break
            count +=1
        return True


if __name__ == '__main__':
    userInput = user_Input()
    check_prime(userInput)
