accum = 0

for n in range(1, 1_001):
    accum += n**n

print(str(accum)[-10:])
