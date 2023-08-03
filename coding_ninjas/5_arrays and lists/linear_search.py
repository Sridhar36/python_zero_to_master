list = [int(x) for x in input("enter the space separated input list: ").split()]
number = int(input("enter the number you are searching for: "))

if number in list:
    print(list.index(number))
else:
    print(-1)
