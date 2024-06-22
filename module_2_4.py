numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []

not_primes = numbers

is_prime = False

for i in numbers:
    for j in range(2, i):
        if i % j == 0:
            is_prime = True
            if is_prime:
                primes.append(i)
            break

for i in numbers:
    for j in range(2, i):
        if i % j == 0:
            is_prime = True
            if is_prime:
                not_primes.remove(i)
            break

for k in numbers:
    for l in range(2, k):
        if k % l == 0:
            is_prime = True
            if is_prime:
                not_primes.remove(k)
            break

print('Primes:', primes)
print('Not_primes:', not_primes)
