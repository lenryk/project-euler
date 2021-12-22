from sympy import primerange, isprime

primes_under_million = [x for x in primerange(1, 999_999)]
truncatable_primes = list()
skip_list = [2, 3, 5, 7]

def truncate_check(string):
    total_count = 0
    for left_pos in range(len(string)):
        if isprime(int(string[left_pos:])):
            total_count += 1
    for right_pos in range(int(len(string)), 0, -1):
        if isprime(int(string[:right_pos])):
            total_count += 1
    if total_count == len(string)*2:
        return True


for prime in primes_under_million:
    if prime not in skip_list:
        if truncate_check(str(prime)):
            truncatable_primes.append(prime)

print(sum(truncatable_primes))
