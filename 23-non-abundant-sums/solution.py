from itertools import product


def proper_divisors(number):
    divisors = list()

    for n in range(1, number):
      if (number % n) == 0:
          divisors.append(n)

    return sum(divisors)

abundant_numbers = [n for n in range(12, 28_124) if proper_divisors(n) > n]  
abundant_sums = set()

for numbers in product(abundant_numbers, abundant_numbers):
    if sum(numbers) <= 28_123:
        abundant_sums.add(sum(numbers))

print(sum([n for n in range(28_124) if n not in abundant_sums]))
