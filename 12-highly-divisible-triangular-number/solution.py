from functools import reduce

def find_divisible(min_divisible):
    n = 1

    while True:
        number = int(n*(n+1)/2)
        step = 2 if number % 2 else 1
        counter = len(set(reduce(list.__add__, 
            ([i, number//i] for i in range(1, int(number**0.5) + 1, step) if number % i == 0))))
        if counter > min_divisible:
            return number

        n += 1

print(find_divisible(500))