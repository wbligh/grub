





"""
        Recipe Web Scraper
           
"""

import requests
from bs4 import BeautifulSoup





url = "https://www.bbcgoodfood.com/recipes/oregano-chicken-squash-traybake"
url_2 = 'https://www.bbcgoodfood.com/recipes/sweet-potatoes-red-pepper-halloumi'



headers = requests.utils.default_headers()  # a bunch of default headers
headers.update({  # add another one to the default set we just created
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',  # firefox v52 useragent
})  # this makes the site thing we're on ubuntu running firefox



def ingredient_list(url):
    results = requests.get(url, headers=headers)

    soup = BeautifulSoup(results.text, "html.parser")

    div=[]

    for EachPart in soup.select('section[class*="ingredients"]'):
        div.append(EachPart.find('ul')) #.find_all('li'))
        items = div[0].find_all('li')
        ingredients = [item.text for item in items]
    return ingredients


ingredients = ingredient_list(url_2)

print([ingredient for ingredient in ingredients])
