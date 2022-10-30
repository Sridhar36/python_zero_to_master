# # import requests
# # import json
# # # assume parsing json format.. get some keys, valuies
# #
# # resp = ""
# # jk = json.dumps(resp)
# # xy = json.loads(jk)
# #
# # try:
# #
# # except:
# #
# # finally:
#
# def pallin(num):
#     chk = str(num)
#     # if chk == chk[::-1]:
#         print("pallin")
#     else:
#         print("not")
#         # num =
#
#
# # 115 =  511
# # 111
# # 121
# # 117
# pallin(1111)

n = int(input("Enter number:"))

'''
121 % 10 = 1  -- gives quotient
121 // 10 = 12 -- gives remainder 
'''


def reversenumber(num):
    reverse = 0
    while num:
        reverse = reverse * 10 + num % 10
        num = num // 10
    return reverse


def pallindrome(n):
    if n == reversenumber(n):
        print("reverse num - ", reversenumber(n))
        print("given num %s is pallindrome " % n)
    else:
        print("given number is not pallindrome going for nearest one")
        while True:
            n = n + 1
            if (n == reversenumber(n)):
                print("nearest pallindrome", n)
                break


pallindrome(n)
