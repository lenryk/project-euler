from sympy import primerange, isprime
from functools import reduce

max_n = 1_000_000
primes = [n for n in primerange(1, max_n)]
output = list()
max_end = 0

for end in range(1, len(primes) + 1):
    if reduce(lambda a, b: a + b, primes[:end]) > max_n:
        max_end = end - 1
        break

for end in range(max_end, 1, -1):
    for start in range(0, end - 1):
        if reduce(lambda a, b: a + b, primes[start:end]) < max_n:
            if isprime(reduce(lambda a, b: a + b, primes[start:end])):
                output.append((reduce(lambda a, b: a + b, primes[start:end]), abs(start - end)))

output.sort(reverse=True, key=lambda x: x[1])
print(output[0])
