all_palindromes = []

for number in range(100, 999+1):
    for inner_number in range(100, 999+1):
        multiplied = str(number * inner_number)
        if multiplied == multiplied[::-1] and len(multiplied) == 6:
            all_palindromes.append(f"{multiplied} ({number} * {inner_number})")
            
all_palindromes.sort()
print(all_palindromes[-1:])