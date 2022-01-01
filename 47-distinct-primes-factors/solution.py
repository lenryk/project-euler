from sympy import primefactors

current_number = 2*3*5*7

while True:
    if len(primefactors(current_number)) == 4:
        current_number += 1
        if len(primefactors(current_number)) == 4:
            current_number += 1
            if len(primefactors(current_number)) == 4:
                current_number += 1
                if len(primefactors(current_number)) == 4:
                    print(current_number, current_number - 1, current_number - 2, current_number - 3)
                    break

    current_number += 1
