triangle_numbers = [n * (n + 1) // 2 for n in range(286, 60_000)]
pentagonal_numbers = [n * (3 * n - 1) // 2 for n in range(166, 50_000)]
hexagonal_numbers = [n * (2 * n - 1) for n in range(144, 50_000)]

print([n for n in triangle_numbers if n in pentagonal_numbers and n in hexagonal_numbers])
