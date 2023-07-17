## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)

n = int(input())
str_n = str(n)

sum_even = 0
sum_odd = 0

# Iterate through each digit in the number
while n > 0:
    digit = n % 10

    # Check if the digit is even or odd
    if digit % 2 == 0:
        sum_even += digit
    else:
        sum_odd += digit

    n = n // 10  # Remove the last digit
