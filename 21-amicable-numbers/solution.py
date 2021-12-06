def proper_divisors(number):
    divisors = list()

    for n in range(1, number):
      if (number % n) == 0:
          divisors.append(n)

    return sum(divisors)

output = list()

for n in range(1, 10_000 + 1):
    test = proper_divisors(n)
    test_second = proper_divisors(test)

    if test_second == n:
      if n != test:
          output.append(n)

print(sum(output))
