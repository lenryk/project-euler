num_product = 1
den_product = 1

for i in range(1, 10):
    for den in range(1, i):
        for num in range(1, den):
            if (10 * num * den) + i * den == (10 * i * num) + den * num:
                num_product *= 10 * num + i
                den_product *= 10 * i + den

print(1 / (num_product / den_product))
