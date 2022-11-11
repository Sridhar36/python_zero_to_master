import requests  # to download html
from bs4 import BeautifulSoup  # to scrap the html

'''
Why do we need these two things?
Well, beautiful soup actually allows us to use the HTML and grab different data.
So it allows us to use that data that we've gathered to do whatever we want to it to scrape it.
But the requests module is actually what allows us to download initially that HTML.

The first thing we're going to do is create a new response variable.
And this response will be the requests and the URL that we want to grab the data from.
So you can think of this as a web browser that we're using without the actual window.
Because this is what Google Chrome is doing underneath the hood.
It's trying to grab the information of that website from a server.
'''

res = requests.get("https://news.ycombinator.com/")
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')  # we are saying convert the response to obj, parse the html content
# print(soup)
# print(soup.body.contents) # to print the content
# print(soup.find_all('div')) # to get all div tags in resp
# print(soup.find_all('a')) # to get all a tags in resp
# print(soup.find_all(id='score_33544883'))  # to get exact entity

'''
Now, one of the best ways, in my opinion, to actually use this soup object is to use the select method on it. And Select
allows us to grab a piece of data from the soup that we just downloaded and created using what we call a CSS selector. 
Now this is a python course, so we're not going to focus too much on CSS selectors. I will link to a resource so you can
learn more about them. But a CSS selector allows us to access this data. Using well CSS selectors. So if I Google here 
CSS selectors you see here that well it's a list of different ways to grab elements on an HTML page. We can use the 
class, the ID, the actual element. 

CSS selectors: tag#id  tag.classname  tag[attribute = 'value']     tag:contains("inner text")
'''

# print(soup.select('.score'))
links = soup.select('.titleline')
votes = soup.select('.score')
# print(votes[0].get('id'))


def create_custom_hn(links, votes):
    hn = []
    '''But within this list, I only want to add the text and none of the HTML. So for example, for the links, we only 
    care about the title.So how can we do that? We want to loop through some things. What we're going to do is say four 
    and we'll use enumerate here. So we're going to have an index and then an item. And in here we're going to enumerate
    remember, we've seen the enumerate before, which gives us an index as well. And we're going to enumerate the links 
    and I'll show you why we want to enumerate in a second. So in here I want to grab the title of each link. By simply 
    doing this, we're going to say '''

    for index, item in enumerate(links):
        title = links[index].getText()
        hn.append(title)
    return hn

print(links)
print(create_custom_hn(links, votes))
