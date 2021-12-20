from sympy import primerange, isprime


def is_circular_prime(num):
    string = str(num)

    for i in range(len(string)):
        string = string[1:]+string[0]
        potencial_circular_prime = int(string)
        if not isprime(potencial_circular_prime):
            return False

    return True

print(len([num for num in primerange(1, 999_999) if is_circular_prime(num)]))
