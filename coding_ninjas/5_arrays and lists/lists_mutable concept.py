li_1 = [1, 2, 3, 4]
li_2 = li_1
li_2[2] = 120

print(li_1)  # will print [1, 2, 120, 4], this is because lists are mutable
# here li_1 and li_2 will point to same memory
