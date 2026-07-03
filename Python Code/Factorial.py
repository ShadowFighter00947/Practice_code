print("Enter a number:-")
n = int(input())

i = 1
answer = 1
while (i <= n):
    answer = answer * i
    i = i + 1

print("Factorial of", n, "is", answer)