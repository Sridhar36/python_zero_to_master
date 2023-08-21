'''
truthy - variables holding some values.
Falsy - variables not holding any value or None objects.
'''

a = 5
b = 'sdfgh'
print(bool(a), bool(b))  # true, true

c = 0
d = ''
print(bool(c), bool(d))  # false, false

# Ternary operator: another way to do conditional logic, also called conditional expressions.,
# condition_if_true if condition else condition_if_false
# it is nice short-hand way
is_friend = True
can_msg = "message allowed " if is_friend else "not allowed to msg"
print(can_msg)  # prints msg allowed since the is_frnd is True

# short circuiting
# Short circuiting can be done using the OR or AND

is_friend = True
is_user = True

# in below if the first condition is true then second condition will not be check
# because when we use OR we are saying anyone should be true.. so interpretor doesnot
# check the second condition.. this is short-cicruiting
# This makes code more efficient
if is_friend or is_user:
    print('best friends forever !!')

# Logical operators
# == > < !=  <= >=
# not  - a keyword and function to check opposite result
print(not (True))

# is vs ==
# is checks for same space
# == checks for same values
print("\nis vs == below")
print(True == 1)  # gives true because, 1 here gets converted to bool(1), where 1 is truthy, so gives true
print('' == 1)  # false
print([] == 1)  # false - [] or '' i.e empty array or empty string are falsy
print(10 == 10.0)  # True.. gets converted int or float and equals
print([] == [])  # true
print("\n now lets try change == with is ")

print("\nis vs == below")
print(True is 1)  # False
print('' is 1)  # False
print([] is 1)  # False
print(10 is 10.0)  # False
print([] is [])  # False
# is gives everything False because is will actually check if the location in memory is same or not


print("\nis vs == below")
print(True is True)  # False
print('1' is '1')  # False
print([] is [])  # False
print(10 is 10)  # False
print([] is [])  # False
