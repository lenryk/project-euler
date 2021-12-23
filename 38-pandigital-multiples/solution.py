digits = list("123456789")
pandigital_multiples = list()


def multiply_num(number):
    concat_number = ""
    n = 1
    while len(str(concat_number)) < 9:
        concat_number += str(number * n)
        n += 1

    if len(concat_number) == 9 and all(x in concat_number for x in digits):
        pandigital_multiples.append(concat_number)


for number in range(1, 999_999):
    multiply_num(number)

print(sorted(pandigital_multiples))
