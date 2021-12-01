numbers = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety",
    1000 : "onethousand",
    }

def numbers_to_text(to_number):
    output = list()

    for number in range (1, to_number + 1):
        int_to_str = str(number)
        single_digits = list(int_to_str)
        if len(int_to_str) == 1 or len(int_to_str) == 4:
            output.append(numbers[number])
        elif len(int_to_str) == 2:
            if number in numbers:
                output.append(numbers[number])
            else:
                output.append(numbers[int(single_digits[0]) * 10] + numbers[int(single_digits[1])])
        elif len(int_to_str) == 3:
            if int(single_digits[1]) == 0 and int(single_digits[2]) == 0:
                output.append(numbers[int(single_digits[0])] + "hundred")
            else:
                if (number % 100)in numbers:
                    output.append(numbers[int(single_digits[0])] + "hundred" + "and" + numbers[(number % 100)])
                else:
                    output.append(numbers[int(single_digits[0])] + "hundred" + "and" + numbers[int(single_digits[1]) * 10] + numbers[int(single_digits[2])])

    return output
    
def sum_letters(numbers_list):
    counter = 0

    for letter in numbers_list:
        counter += len(letter)
    
    return counter

print(sum_letters(numbers_to_text(1000)))
