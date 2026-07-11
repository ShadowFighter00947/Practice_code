# code to create username from given email.
email = input('Enter your email:- ')
for c in email:
    if (c == '@'):
        break
    print(c, end = '')