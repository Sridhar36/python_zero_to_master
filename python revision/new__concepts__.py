# shallow vs deep copy
# applies to all mutable data types

import copy

a = [1, 2, [10, 20]]
b = copy.copy(a)

b[2].append(30)

print(a)  # [1, 2, [10, 20, 30]]
print(b)  # [1, 2, [10, 20, 30]]



# import copy
#
# a = [1, 2, [10, 20]]
# b = copy.deepcopy(a)
#
# b[2].append(30)
#
# print(a)  # [1, 2, [10, 20]]
# print(b)  # [1, 2, [10, 20, 30]]
