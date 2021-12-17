products = set()
digits_to_check = set("123456789")


def find_numbers(start, end):
    for i in range(start, end):
        for j in range(99, 9999):
            number = str(i) + str(j) + str(i * j)
            if len(number) == 9 and set(number) == digits_to_check:
                products.add(i * j)
            elif len(number) > 9:
                break


find_numbers(0, 9)
find_numbers(9, 99)

print(sum(products))
