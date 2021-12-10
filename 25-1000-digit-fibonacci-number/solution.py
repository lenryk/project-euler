def fibonacci_of(n):
    if not (isinstance(n, int) and n >= 0):
        raise ValueError(f'Positive integer number expected, got "{n}"')

    previous, fib_number = 0, 1
    for _ in range(2, n + 1):
        previous, fib_number = fib_number, previous + fib_number

    return str(fib_number)

n = 1
while len(fibonacci_of(n)) != 1_000:
    n += 1

print(n)
