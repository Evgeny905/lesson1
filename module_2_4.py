numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []

not_primes = []

is_prime = False


for i in numbers:
    for j in range(2, i-1):
        if i % j == 0:
            primes = [i]
        else: not_primes = [i]
        print(not_primes)
