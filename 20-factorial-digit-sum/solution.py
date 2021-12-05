import math


factorial = math.factorial(100)
factorial = list(str(factorial))
factorial = [int(n) for n in factorial]

print(sum(factorial))