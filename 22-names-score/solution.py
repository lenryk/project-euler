def calc_score(name):
    name = list(name)
    score = 0

    for n in name:
        score += (ord(n) - 64)

    return score

with open("names.txt", "r") as file:
    names = file.read()
    names = names.replace('"', "")
    names = names.split(",")
    names = sorted(names)

output = list()

for index, name in enumerate(names):
    output.append(calc_score(name) * (index + 1))

print(sum(output))
