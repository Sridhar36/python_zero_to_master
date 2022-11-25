import requests  # to download html
from bs4 import BeautifulSoup  # to scrap the html
import pprint  # built in module for printing to console neatly

res = requests.get("https://news.ycombinator.com/")
res2 = requests.get("https://news.ycombinator.com/news?p=2")
soup = BeautifulSoup(res.text, 'html.parser')  # we are saying convert the response to obj, parse the html content
soup2 = BeautifulSoup(res2.text, 'html.parser')
links = soup.select('.titleline')
# votes = soup.select('.score')
subtext = soup.select('.subtext')
links2 = soup2.select('.titleline')
subtext2 = soup2.select('.subtext')

addedlinks = links + links2
addsubtexts = subtext + subtext2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


'''
sorted(hn list) - this gives error:

We get an error here, and if we read the error says type error, not supported between instances of dict and dict. What 
does that mean?
Well, we're trying to sort items in a list, but they're all dictionaries. So Python is saying, hey, I don't understand.
How do you want me to sort it? Do you want me to sort it by title, by link, by votes? You got to tell me. And this is a
common pattern with sorted that you'll just have to get used to. We're going to use a lambda function. Our second 
parameter is simply going to be the key that we want to sort by. And that key that we want to sort by is well votes, 
right? So all we going to do is say Lambda. And say key. And this key that we're going to sort by is going to be votes.
So that if I save this and run this again.Look that.I have everything sorted by votes.
'''


def create_custom_hn(links, votes):
    hn = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)  # None here is default value, just in case if we dont
        # have any value then it gets defaulted to None

        vote = subtext[index].select('.score')
        if len(vote):  # if length is not zero
            points = int(vote[0].getText().replace(" points", ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})

    return sort_stories_by_votes(hn)


print(links)
# pprint.pprint(create_custom_hn(links, subtext))  # to print neatly
pprint.pprint(create_custom_hn(addedlinks, addsubtexts))
