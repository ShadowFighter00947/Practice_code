num = int(input('Please enter a number:-'))
# Getting input from user and converting it into an integer.

if (num % 5 == 0):
    if (num % 10 == 0 ):
        print('0')
    else:
        print('5')
else:
    print('other')