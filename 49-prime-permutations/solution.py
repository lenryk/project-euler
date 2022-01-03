from sympy import primerange
from collections import Counter


for prime in primerange(1_488, 10_001):
    if (prime + 3330) in primerange(1_488, 10_001):
        if (prime + (3330 * 2)) in primerange(1_488, 10_001):
            if Counter(str(prime + 3330)) == Counter(str(prime + (3330 * 2))):
                print(prime, prime + 3330, prime + (3330 * 2))
                break
