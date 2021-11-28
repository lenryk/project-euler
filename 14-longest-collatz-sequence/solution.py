def even_number(n):
    if n % 2 == 0:
        return (n / 2)
    else:
        raise TypeError

def odd_number(n):
    if n % 2 == 1:
        return (3 * n) + 1
    else:
        raise TypeError

def calculate_chain(n):
    counter = 1

    while n != 1:
        if n % 2 == 0:
            n = even_number(n)
            counter += 1
        else:
            n = odd_number(n)
            counter += 1

    return counter

def find_largest_chain(n):
    largest_result = [0, 0]
    while n != 0:
        result = calculate_chain(n)
        if result > largest_result[0]:
            largest_result = [result, n]
        n -= 1

    print(largest_result)

find_largest_chain(999_999)
