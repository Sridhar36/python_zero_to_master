import random


# we can test this unit
def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are genius!')
            # break this gives an error since we are outside the loop.. that is we dont have any while loop or for loop
            # running. So we can use return instead
            return True
    else:
        print("hey bozo, I said 1 ~ 10")
        return False


if __name__ == 'main':
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input("Enter your number 1 ~ 10: "))
            if (run_guess(guess, answer)):
                break
        except ValueError:
            print('Kindly, enter numbers only!')
            continue
