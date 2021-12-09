import itertools


perms = list()
counter = 0
for n in itertools.permutations(range(0, 10), 10):
    if counter < 1_000_000:
        perms.append(n)
        counter += 1

perms.sort()
print(perms[999_999])
