import re

a = None
while a == None:
    password = input('Enter your pass (use a-Z@#$% and min 8 strings): ')
    password_patern = re.compile(r'[a-zA-Z0-9@%$#]{8,}\d$')
    '''
    [a-zA-Z0-9@%$#]{8,}\d$  
    [a-zA-Z0-9@%$#] -  string has to have the collection of of chars of a-z or A-z or 0-9 or @%$# 
    {8,}  - string should have minimum 8 chars
    \d to match decimal digit
    \d$ - the string should end with digit
    '''
    a = password_patern.fullmatch(password)
    if a != None:
        break
    else:
        print('You wrote wrong password')
print('You may use the password')
