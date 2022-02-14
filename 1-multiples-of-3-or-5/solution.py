output = []

for n in range(1000):
    if n % 3 == 0 or n % 5 == 0:
        output.append(n)
print(sum(output))
