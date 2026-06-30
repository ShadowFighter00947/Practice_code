time = int(input('Please enter time:'))
higher = int(input('Define higher:'))

if (time >= higher):
    price = int(input('Please enter price:'))
    higher = int(input('Define Higher:'))
    if (price >= higher):
        print('Train')
    else:
        print('Coach')
else:
    price = int(input('Please enter price:'))
    higher = int(input('Define higher:'))
    if (price >= higher):
        print('Daytime Flight')
    else:
        print('Red Eye Flight')
print('Arrive at city B')