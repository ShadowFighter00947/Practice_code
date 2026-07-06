n = int(input('Enter a number: '))
ans = 0

for i in range (n):
# Default range start from 0 and ends at n-1.
    ans = ans + i

print('Addition of', n, 'number is', ans)