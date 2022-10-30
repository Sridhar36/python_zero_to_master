def highest_even(a):
    '''
    This function finds the highest even number from given list
    :param a: input array
    :return: highest even
    '''
    new_a = []
    for val in a:
        if val % 2 == 0:
            new_a.append(val)
    return max(new_a)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(highest_even(arr))

# walrus operator ( := )
# eg:

a = 'helloooooooooo'

# here we are using len() twice
if (len(a) > 10):
    print(f"too long {len(a)} elements")

# now lets try above using walrus operator
if ((n := len(a)) > 10):
    print(f"too long {n} elements")
