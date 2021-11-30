def sum_individual_numbers(n):
    n = str(n)
    single_digits = list(n)
    sum = 0
    
    for number in single_digits:
        sum += int(number)

    print(sum)

sum_individual_numbers(2**1000)