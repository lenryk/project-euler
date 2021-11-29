import math


# combinations calculator
# 2 x 2 grid has 6 routes
# use combinations formula

def calc_combinations(grid_size):
    sample = grid_size * 2
    return math.factorial(sample) // ((math.factorial(grid_size) * math.factorial((sample - grid_size))))

print(calc_combinations(20))