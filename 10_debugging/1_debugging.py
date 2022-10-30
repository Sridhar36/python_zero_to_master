# 10_debugging


# 1. linting - allows to check errors before itself, like below num throwing error
# num + 4

# 2.  read errors
# like below gives type error
# 4 + 'dgdhjkdjh'
# below gives syntax error
# 4 + 'dgdhjkdjh

# print is a quick and easy way to debug

# 3. PDB - Python debugger - builtin module for 10_debugging

import pdb

def add(num1, num2):
    pdb.set_trace()  #this tops code and allow you to test
    # print(num1, num2)
    return num1 + num2

print(add(4,'jk'))


'''
in cmd if you type help - gives all help that it cu
'''