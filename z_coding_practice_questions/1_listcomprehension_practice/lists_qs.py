'''
Use for the questions below:
* nums = [i for i in range(1,1001)]
* string = "Practice Problems to Drill List Comprehension in Your Head."

-Find all of the numbers from 1–1000 that are divisible by 8
-Find all of the numbers from 1–1000 that have a 6 in them
-Count the number of spaces in a string (use string above)
-Remove all of the vowels in a string (use string above)
-Find all of the words in a string that are less than 5 letters (use string above)
-Use a dictionary comprehension to count the length of each word in a sentence (use string above)
-Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit besides 1 (2–9)
-For all the numbers 1–1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by'''

string = "Practice Problems to Drill List Comprehension in Your Head."
nums = [i for i in range(1, 1001)]

# 1
print([i for i in nums if (i % 8 == 0)])
# 2
print([i for i in nums if '6' in str(i)])
# 3
count = 0
for i in string:
    if i == ' ':
        count += 1
print(count)

# or
print(len([char for char in string if char == " "]))

# 4. Remove all of the vowels in a string (use string above)
newstr = ""
for i in string:
    if i in ['a', 'e', 'i', 'o', 'u']:
        continue
    else:
        newstr += i
print(newstr)
# or
print("".join([char for char in string if char not in ["a", "e", "i", "o", "u"]]))

# 5.Find all of the words in a string that are less than 5 letters (use string above)
newstr = string.split(" ")
print([word for word in newstr if len(word) <= 5])

# 6. Use a dictionary comprehension to count the length of each word in sentance (use string above)
words = string.split(" ")
print({word: len(word) for word in words})

# 7. Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any
# single digit besides 1 (2–9)
print([num for num in nums if True in [True for divisor in range(2, 10) if num % divisor == 0]])

# 8. For all the numbers 1–1000, use a nested list/dictionary comprehension to find the highest single digit any of the
# numbers is divisible by'''
q8_answer = {num: max([divisor for divisor in range(1, 10) if num % divisor == 0]) for num in nums}
print(q8_answer)
