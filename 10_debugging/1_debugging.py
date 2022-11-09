''' 10_debugging
1. linting - allows to check errors before itself, like below num throwing error
            num + 4
2.  read errors -  like in this case gives type error - 4 + 'dgdhjkdjh'
         4 + 'dgdhjkdjh -  gives syntax error
3.  print is a quick and easy way to debug
4. PDB - Python debugger - builtin module for 10_debugging

udmey
https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16112803#notes
'''
import pdb


def add(num1, num2):
    pdb.set_trace()  # this stops code and allow you to test
    # print(num1, num2)
    return num1 + num2

print(add(4, 'jk'))

'''
in cmd if you type help - gives all help that it cu
'''
