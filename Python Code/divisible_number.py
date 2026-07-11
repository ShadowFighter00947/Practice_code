num = int(input('Enter a number'))
if (num <= 1000):
    for x in range(1001):
        if(x % num == 0):
            print(x)
else:
    print('Out of range')