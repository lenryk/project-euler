def main():
    fith_power_sums = list()
    for n in range(2, 1_000_000):
        total_sum = list()
        int_numbers = split_numbers(n)
        for digit in int_numbers:
            total_sum.append(digit ** 5)
        if sum(total_sum) == n:
            fith_power_sums.append(n)
    
    print(sum(fith_power_sums))

def split_numbers(numbers):
    output = list(str(numbers))
    return [int(x) for x in output]

main()
