from sympy import primerange, isprime


odd_composite = [n for n in range(33, 10_001, 2) if not isprime(n)]
primes = [n for n in primerange(1, 10_001)]


def check_conjecture(prime, composite):
    counter = 0
    for i in range(1, 101):
        if prime + 2 * i ** 2 == composite:
            return True
        else:
            counter += 1

    if counter == 100:
        return False


for composite in odd_composite:
    valid = False
    for prime in primes:
        if check_conjecture(prime, composite):
            valid = True
            break

    if not valid:
        print(composite)
