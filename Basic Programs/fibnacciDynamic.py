fibcache = {}
value = 0

def fib(num):
    global fibcache
    global value
    if num in fibcache:
        return fibcache[num]
    if num <= 2:
        fibcache[num] = 1
    else:
        fibcache[num] = fib(num-1) + fib(num-2)
    return fibcache[num]


if __name__ == '__main__':
    num = int(input('Enter the number : '))
    print(fib(num))

