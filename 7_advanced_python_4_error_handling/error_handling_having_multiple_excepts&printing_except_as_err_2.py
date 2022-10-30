def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:  # catch the type error as err, so that we can use in excpet for printing the error
        # print("please enter a number" + err)  # -> this will throw error, bcoz err is an error object.. you cannot add.. instead f string to print
        print(f'please enter numbers, to avoid, error:  {err}')


print(sum(1, '2'))


def divide(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:  # we can wrap the exceptions
        print(err)


print(divide(0, 0))
print(divide('s', 3))
