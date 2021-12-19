from math import factorial
digit_factorials = list()


for n in range(3, 9_999_999):
    product = 0
    for digit in list(str(n)):
        product += factorial(int(digit))
    if product == n:
        digit_factorials.append(n)

print(digit_factorials)
