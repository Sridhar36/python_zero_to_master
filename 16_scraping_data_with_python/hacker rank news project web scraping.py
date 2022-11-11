import requests  # to download html
from bs4 import BeautifulSoup  # to scrap the html
import pprint  # built in module for printing to console neatly

res = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(res.text, 'html.parser')  # we are saying convert the response to obj, parse the html content

links = soup.select('.titleline')
# votes = soup.select('.score')
subtext = soup.select('.subtext')


def create_custom_hn(links, votes):
    hn = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)  # None here is default value, just in case if we dont
        # have any value then it gets defaulted to None

        vote = subtext[index].select('.score')
        if len(vote):  # if length is not zero
            points = int(vote[0].getText().replace(" points", ''))
            if points > 100:
                hn.append({'title': title, 'link': href, 'votes': points})

    return hn


print(links)
pprint.pprint(create_custom_hn(links, subtext))  # to print neatly
