# # # import requests
# # # import json
# # # # assume parsing json format.. get some keys, valuies
# # #
# # # resp = ""
# # # jk = json.dumps(resp)
# # # xy = json.loads(jk)
# # #
# # # try:
# # #
# # # except:
# # #
# # # finally:
# #
# # def pallin(num):
# #     chk = str(num)
# #     # if chk == chk[::-1]:
# #         print("pallin")
# #     else:
# #         print("not")
# #         # num =
# #
# #
# # # 115 =  511
# # # 111
# # # 121
# # # 117
# # pallin(1111)
#
# n = int(input("Enter number:"))
#
#
# def reversenumber(num):
#     reverse = 0
#     while num:
#         reverse = reverse * 10 + num % 10
#         num = num // 10
#     return reverse
#
#
# def pallindrome(n):
#     if n == reversenumber(n):
#         print("reverse num - ", reversenumber(n))
#         print("given num %s is pallindrome " % n)
#     else:
#         print("given number is not pallindrome going for nearest one")
#         while True:
#             n = n + 1
#             if (n == reversenumber(n)):
#                 print("nearest pallindrome", n)
#                 break
#
# pallindrome(n)


# print(121%10)
# print(121//10)

import requests

def find_industry(company_name):
    """Fetches the industry domain of a company using DuckDuckGo API."""
    try:
        url = f"https://api.duckduckgo.com/?q={company_name}+company+industry&format=json"
        response = requests.get(url).json()
        
        related_topics = response.get("RelatedTopics", [])
        print(related_topics)
        for topic in related_topics:
            if "Text" in topic and "industry" in topic["Text"].lower():
                return topic["Text"]  # Returns text containing industry info

        return "Unknown"
    except Exception as e:
        print(f"Error fetching industry: {e}")
        return "Unknown"
    
print(find_industry("TCS"))