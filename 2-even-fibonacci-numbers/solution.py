def fibonacci_of(n):
    if not (isinstance(n, int) and n >= 0):
        raise ValueError(f'Positive integer number expected, got "{n}"')

    previous, fib_number = 0, 1
    for _ in range(2, n + 1):
        previous, fib_number = fib_number, previous + fib_number

    return fib_number

fib = [fibonacci_of(n) for n in range(1,33+1)]
print(sum([n for n in fib if n % 2 == 0]))