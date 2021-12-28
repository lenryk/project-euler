import itertools

zero_nine_pandigitals = [x for x in itertools.permutations("1234567890", 10)]
division = [1, 2, 3, 5, 7, 11, 13, 17]
valid_pandigitals = list()


def find_indexes(number, indexes):
    index_numbers = list()
    for n in indexes:
        index_numbers.append(number[n])
    index_numbers = [str(x) for x in index_numbers]
    return int("".join(index_numbers))


def check_all_indexes(number):
    division_counter = 0
    for n in range(1, 8):
        sub_number = find_indexes(number, range(n, n + 3))
        if sub_number % division[n] == 0:
            division_counter += 1

    if division_counter == 7:
        number_int = [str(x) for x in number]
        valid_pandigitals.append(int("".join(number_int)))


for pandigital in zero_nine_pandigitals:
    # Since d2d3d4 has to be divisible by 2 it means that d4 must be even.
    if int(pandigital[3]) % 2 == 0:
        check_all_indexes(pandigital)

print(sum(valid_pandigitals))
