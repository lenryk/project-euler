import sympy


def find_n_prime_number(max_num):
    return sum(list(sympy.primerange(0, max_num)))

print(find_n_prime_number(2_000_000))
