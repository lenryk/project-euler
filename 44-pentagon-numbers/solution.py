from itertools import combinations


pentagon_numbers = list()
pentagonals = set(n*(3*n-1)//2 for n in range(1, 5_000))
pentagon_combos = combinations(pentagonals, 2)

for n1, n2 in pentagon_combos:
    if n1 + n2 in pentagonals and abs(n2 - n1) in pentagonals:
        pentagon_numbers.append(abs(n2 - n1))

print(sorted(pentagon_numbers))
