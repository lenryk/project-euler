def smallest_multiple():
    for number in range(1, 1_000_000_000):
        counter = 0
        largest_num = 20
        for division in range(1, largest_num + 1):
            if number % division == 0:
                counter += 1
            if counter == largest_num:
                return number
                
print(smallest_multiple())
