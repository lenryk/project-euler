max_len = 0
max_digit = 0

def fraction_to_decimal(denominator):
    output = ""
    store = {}
    rem = 1 % denominator
 
    while ((rem != 0) and (rem not in store)):
        store[rem] = len(output)
        rem = rem * 10

        res_part = rem // denominator
        output += str(res_part)
 
        rem = rem % denominator
 
    if (rem == 0):
        return ""
    else:
        return output[store[rem]:]
 
for n in range (1, 1_001):
    decimal = fraction_to_decimal(n)

    if len(decimal) > max_len:
        max_len = len(decimal)
        max_digit = n

print(max_len, max_digit)