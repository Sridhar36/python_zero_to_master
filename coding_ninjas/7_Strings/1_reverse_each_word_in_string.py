string = "Welcome to Coding Ninjas"

words = string.split()
words_reversed = [word[::-1] for word in words]
reversed_string = " ".join(words_reversed)
print(reversed_string)

print(" ".join([word[::-1] for word in string.split()]))


