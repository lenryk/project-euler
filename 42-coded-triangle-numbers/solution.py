triangle_numbers = [int(0.5*n*(n+1)) for n in range(1, 100)]
parsed_words = list()
word_numbers = list()
triangle_numbers_count = 0

with open("p042_words.txt") as words:
    words = words.read()
    words = words.split(",")
    for word in words:
        parsed_words.append(list(word[1:-1]))

for word in parsed_words:
    word_as_list = list(word)
    word_as_numbers = list()
    for char in word_as_list:
        word_as_numbers.append(ord(char) - 64)

    word_numbers.append(sum(word_as_numbers))

for number in word_numbers:
    if number in triangle_numbers:
        triangle_numbers_count += 1

print(triangle_numbers_count)
