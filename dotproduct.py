def dot_product(a, b):
    return sum(x * y for x, y in zip(a, b))

print(dot_product([1, 2, 3], [4, 5, 6]))

