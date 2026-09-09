# The above code is to understand recursion.
# When a function calls itself in the function this is called recursion.


def sum(n):
# verified.
    if (n==1):
        return 1
    else:
        return sum(n-1)+n

def comp(p,n):
#verified.
    if (n==1):
        return (p*1.1)
    else:
        return (comp(p,n-1))*(1.1)

def fact(n):
#verified.
    if(n==1):
        return 1
    else:
        return fact(n-1)*n

print(sum(10))
print(comp(2000,3))
print(fact(5))

