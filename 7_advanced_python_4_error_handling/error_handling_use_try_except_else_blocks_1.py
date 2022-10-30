  # Error handling

# sample usage
# try:  # will try run this code in try block, only if any error occur control get into except block
#     age = int(input("what is your age? "))
# except:  # if there is any error then access will go into the except block and does whatever inside except
#     print("please enter a number")

# built in exceptions list: https://docs.python.org/3/library/exceptions.html
# We can directly mention these in the except

while True:  # using while loop to end on receiving the valid value
    try:
        age = int(input("what is your age? "))
    except ValueError:
        print('please enter a Number')
    else:  # if value is number then we can break loop
        print("Thanks!!")
        break
