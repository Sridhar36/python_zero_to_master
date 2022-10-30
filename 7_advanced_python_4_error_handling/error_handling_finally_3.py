'''
finally is used when to print something no matter whats the result
uses:
'''

while True:  # using while loop to end on receiving the valid value
    try:
        age = int(input("wha is your age? "))
    except ValueError:
        print('please enter a Number')
    else:  # if value is number then we can break loop
        print("Thanks!!")
        break
    finally:
        print("am done")

