# Exercise

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

for val in picture:
    for binary in val:
        if binary == 0:
            print(' ', end='')
        elif binary == 1:
            print('*', end='')
    print()

# better code format for the code above
fill = '*'  # changing variable possible by declaring them here.. like we can replace * with $ easily
empty = ' '
for row in picture:
    for pixel in row:
        if pixel:
            print(fill, end='')
        else:
            print(empty, end='')
    print('')

# 2. find duplicates in a list

somelist = ['a', 'b', 'c', 'd', 'b', 'm', 'n', 'n']
duplicates = []
for value in somelist:
    if somelist.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
