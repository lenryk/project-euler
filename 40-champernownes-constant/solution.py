concat_number = "0."

for number in range(1, 1_000_000):
    concat_number += str(number)

indexes = [2, 11, 101, 1_001, 10_001, 100_001, 1_000_001]
index_product = 1

for index in indexes:
    index_product *= int(concat_number[index])

print(index_product)
