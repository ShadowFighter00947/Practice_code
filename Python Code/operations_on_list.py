def list_mini(l):
    mini = l[0]
    for i in range(len(l)):
        if (l[i] < mini):
            mini = l[i]
    return mini

def list_maxi(l):
    maxi = l[0]
    for i in range(len(l)):
        if (l[i] > maxi):
            maxi = l[i]
    return maxi

def list_appendbefore(l,z):
    newl = []
    for i in range(len(z)):
        newl.append(z[i])
    for i in range(len(l)):
        newl.append(l[i])
    return newl

def list_appendafter(l,z):
    newl = []
    for i in range(len(l)):
        newl.append(l[i])
    for i in range(len(z)):
        newl.append(z[i])
    return newl

def list_average(l):
    sum = 0
    for i in range(len(l)):
        sum = sum + l[i]
    average = sum / len(l)
    return average

l = [10,20,40,-15,100,58,-1000]
z = [100,200,300]


print('Maximum value of list l is ', list_maxi(l))
print('Minimum value of list l is ', list_mini(l))
print('Maximum value of list l is ', list_maxi(z))
print('Minimum value of list l is ', list_mini(z))
print('List z append before list l is ', list_appendbefore(l,z))
print('List z append after list l is ', list_appendafter(l,z))
print('Average of list l is ', list_average(l))
print('Average of list z is ', list_average(z))