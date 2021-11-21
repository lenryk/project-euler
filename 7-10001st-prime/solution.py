def find_n_prime_number(n):
    counter = 2
    number = 3

    while n + 1 != counter:
        if check_prime(number) <= 2:
            # print("prime number", number)
            counter+= 1
        number+= 1

    return number - 1

def check_prime(number):
    counter = 1
    
    for prime in range(2, number + 1):
        if (number % prime) == 0:
            counter+= 1
        elif counter > 2:
            break

    return counter

print(find_n_prime_number(10_001))