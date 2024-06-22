numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []

not_primes = []

is_prime = False


for i in numbers:
    for j in range(2, i):
        if i % j == 0:
            is_prime = True
            if is_prime:
                primes.insert(i)
            else:
                not_primes.insert(i)
            break
print(primes)
