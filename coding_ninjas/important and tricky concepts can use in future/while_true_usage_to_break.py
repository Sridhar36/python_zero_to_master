# Write your code here
while True: # to use break we need a loop
    choice = int(input())

    if choice == 1:
        num1 = int(input())
        num2 = int(input())
        print(num1 + num2)

    elif choice == 2:
        num1 = int(input())
        num2 = int(input())
        print(num1 - num2)

    elif choice == 3:
        num1 = int(input())
        num2 = int(input())
        print(num1 * num2)

    elif choice == 4:
        num1 = int(input())
        num2 = int(input())
        print(num1 / num2)

    elif choice == 5:
        num1 = int(input())
        num2 = int(input())
        print(num1 % num2)

    elif choice == 6:
        break

    else:
        print("Invalid Operation")
