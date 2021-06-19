


'''

Generalised Scraper

'''


import requests
from bs4 import BeautifulSoup


url = 'https://www.olivemagazine.com/recipes/vegetarian/spiced-carrot-and-lentil-soup/'
url_2 = 'https://www.bbcgoodfood.com/recipes/sweet-potatoes-red-pepper-halloumi'

headers = requests.utils.default_headers()  # a bunch of default headers
headers.update({  # add another one to the default set we just created
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',  # firefox v52 useragent
})  # this makes the site thing we're on ubuntu running firefox


def clean(str):
    str = str.strip('\n')
    str = str.strip('\t')
    return str



def retrieve(url):
    results = requests.get(url, headers=headers)
    return BeautifulSoup(results.text, "html.parser")

def ingredients(url):
    Heading = retrieve(url).select('h3[class*="ingredients"]')
    ls = Heading[0].find_next_sibling('ul') 
    items = ls.find_all('li')
    ingredients = [clean(item.text) for item in items]
    return ingredients


