import requests



def add(*val):
    print(type(val))
add(2,3)
add('helo', 'hi')

x =True
y = False
z = False

if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and z:
    print(3)
else:
    print(4)

x1 = lambda a: a+10
print(x1)
