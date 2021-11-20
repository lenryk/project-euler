natural_numbers = 100

def calc_natural_numbers():
    natural_numbers_sum = []
    for number in range(1, natural_numbers + 1):
        natural_numbers_sum.append(number ** 2)
    return sum(natural_numbers_sum)

def calc_square_sum():
    square_sum  = 0
    for number in range(1, natural_numbers +1):
        square_sum += number
    return square_sum ** 2

def sums_difference():
    return calc_square_sum() - calc_natural_numbers()

print(sums_difference())
