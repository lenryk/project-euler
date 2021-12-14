def main(max):
    distinct_terms = set()

    for a in range(2, max + 1):
        for b in range(2, max + 1):
            distinct_terms.add(a**b)

    print(len(distinct_terms))

main(100)
