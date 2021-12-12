from sympy import isprime, primerange


max_consecutive = 0
for a in range(-1_000, 1_000):
    for prime_number in primerange(1, 1_000):
        n = 0
        consecutive = 0
        while isprime(n ** 2 + a * n + prime_number):
            n += 1
            consecutive += 1
        if consecutive > max_consecutive:
            max_consecutive = consecutive
            max_number = a * prime_number

print(max_number, max_consecutive)
