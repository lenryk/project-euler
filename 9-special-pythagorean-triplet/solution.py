def find_triplet():
    for n in range(1, 500):
        if 1000 * (500 - n) % (1000 - n) == 0:
            second = 1000 * (500 - n) / (1000 - n)
            third = ((second**2) + (n**2))**0.5
            return int(n * second * third)

print(find_triplet())