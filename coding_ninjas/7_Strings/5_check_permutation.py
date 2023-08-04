string1 = "srting"
string2 = "strnig"


def isPermutation(string1, string2):
    # Your code goes here
    if len(string1) != len(string2):
        return False

    str1_ascii = sum([ord(x) for x in string1])
    str2_ascii = sum([ord(x) for x in string2])

    if str1_ascii == str2_ascii:
        return True


print(isPermutation(string1, string2))
