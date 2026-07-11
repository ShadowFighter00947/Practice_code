#Accept a positive integer n, with n>1 , as input from the user and print all the prime factors of n in ascending order.
n = abs(int(input()))

for i in range(2, n + 1):
    if n % i == 0:          # i is a factor of n
        is_prime = True

        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            print(i)

