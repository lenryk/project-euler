def right_upper_diagnol(max):
    n = 3
    output = list()
    while n <= max:
        output.append(n**2)
        n += 2

    return output

def left_bottom_diagnol(max):
    n = 3
    distance = 1
    output = list()
    while n <= max:
        output.append(n**2 - (4 * distance))
        n += 2
        distance += 1
    
    return output

def left_upper_diagnol(max):
    n = 3
    distance = 1
    output = list()
    while n <= max:
        output.append(n**2 - (2 * distance))
        n += 2
        distance += 1
    
    return output

def right_bottom_diagnol(max):
    n = 3
    distance = 1
    output = list()
    while n <= max:
        output.append(n**2 - (6 * distance))
        n += 2
        distance += 1

    return output

def main(size):
    all_diagnols = right_upper_diagnol(size) + left_bottom_diagnol(size) + left_upper_diagnol(size) + right_bottom_diagnol(size)

    print(sum(all_diagnols) + 1)

main(5)