
# Using a for loop
pairs_for_loop = []
for x in range(3):
    for y in range(2):
        pairs_for_loop.append((x, y))

# Using list comprehension
pairs_list_comprehension = [(x, y) for x in range(3) for y in range(2)]

print(pairs_for_loop)               # Output: [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
print(pairs_list_comprehension)     # Output: [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]



# Using a for loop
evens_for_loop = []
for x in range(10):
    if x % 2 == 0:
        evens_for_loop.append(x)

# Using list comprehension
evens_list_comprehension = [x for x in range(10) if x % 2 == 0]

print(evens_for_loop)               # Output: [0, 2, 4, 6, 8]
print(evens_list_comprehension)     # Output: [0, 2, 4, 6, 8]


# Using a for loop
squares_for_loop = []
for x in range(5):
    squares_for_loop.append(x**2)

# Using list comprehension
squares_list_comprehension = [x**2 for x in range(5)]

print(squares_for_loop)              # Output: [0, 1, 4, 9, 16]
print(squares_list_comprehension)    # Output: [0, 1, 4, 9, 16]
