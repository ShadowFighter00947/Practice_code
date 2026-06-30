marks = int(input('Please enter your marks:'))
# Getting input from user and converting it into an integer.

if (marks >= 0  and marks <=100):
    if (marks >= 90):
        print('A')
    elif (marks >= 80):
        print ('B')
    elif (marks >= 70):
        print('C')
    elif (marks >= 60):
        print('D')
    else:
        print('E')
else:
    print('Invalid Output')