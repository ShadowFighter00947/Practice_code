alpha = 'abcdefghijklmnopqrstuvwxyz'

s = 'amjad'
# s variable takes word from user to convert it into a code.

t = ''
i = 0
k = 1
# k takes a number from user to conver into code and stores in 't' variable. 
#Example:- word = india, k = 1
#then 't' = joejb, will be the coded word.

t = t + (alpha[(((alpha.index(s[i]))+k)%26)])
t = t + (alpha[(((alpha.index(s[i+1]))+k)%26)])
t = t + (alpha[(((alpha.index(s[i+2]))+k)%26)])
t = t + (alpha[(((alpha.index(s[i+3]))+k)%26)])
t = t + (alpha[(((alpha.index(s[i+4]))+k)%26)])

print(t)