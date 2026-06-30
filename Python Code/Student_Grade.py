marks = int(input('Please enter your marks:'))
# Getting input from user and converting it into an integer.

if (marks >= 0 and marks <=100):
    if (marks >= 90):
        print('A')
    if (marks >= 80 and marks < 90):
        print('B')
    if (marks >=70 and marks < 80):
        print('C')
    if (marks >=60 and marks < 70):
        print('D')
    if (marks < 60):
        print('E')
else:
    print('Invalid Output') 