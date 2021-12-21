def check_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


palindromes = list()

for number in range(1, 999_999):
    if check_palindrome(str(number)):
        if check_palindrome(bin(number)[2:]):
            palindromes.append(number)

print(sum(palindromes))
