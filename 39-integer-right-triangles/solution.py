from collections import Counter


perimeters = list()

for n1 in range(1, 500):
    for n2 in range(n1, 500):
        n3 = (n1 ** 2 + n2 ** 2) ** 0.5
        if int(n3) == n3 and n1 + n2 + n3 <= 1000:
            perimeters.append(int(n1 + n2 + n3))

print(Counter(perimeters).most_common(1))
