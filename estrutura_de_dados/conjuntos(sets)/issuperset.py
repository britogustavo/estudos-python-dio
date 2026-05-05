conjunto_a = {1, 2, 3, 4, 5, 6, 7, 8}
conjunto_b = {3, 4, 5}

print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))

print(conjunto_a >= conjunto_b)
print(conjunto_b >= conjunto_a)