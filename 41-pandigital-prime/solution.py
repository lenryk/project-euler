from sympy import primerange


generated_primes = [str(x) for x in primerange(1, 7_654_321)]
pandigital_primes = list()


for prime in generated_primes:
    digits = [str(x) for x in range(1, len(prime) + 1)]
    prime_list = list(prime)

    if all(elem in prime_list for elem in digits):
        pandigital_primes.append(prime)

print(max(pandigital_primes))
