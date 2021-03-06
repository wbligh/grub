





"""
        Recipe Web Scraper
           
"""

import requests
from bs4 import BeautifulSoup





url = "https://www.bbcgoodfood.com/recipes/oregano-chicken-squash-traybake"
url_2 = 'https://www.bbcgoodfood.com/recipes/sweet-potatoes-red-pepper-halloumi'
url_3 = 'https://www.bbcgoodfood.com/recipes/pepper-steak-with-noodles'
url_4 = 'https://www.bbcgoodfood.com/recipes/pasta-alla-norma'
url_5 = 'https://www.bbcgoodfood.com/recipes/pork-fennel-burgers-fennel-slaw'





def parse(url): 
    headers = requests.utils.default_headers()  # a bunch of default headers
    headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})  # this makes the site thing we're on ubuntu running firefox
    results = requests.get(url , headers=headers)
    return BeautifulSoup(results.text, "html.parser")

def ingredient_list(url):
    soup = parse(url)
    div=[]
    for EachPart in soup.select('section[class*="ingredients"]'):
        div.append(EachPart.find('ul')) #.find_all('li'))
        items = div[0].find_all('li')
        ingredients = [item.text for item in items]
    return ingredients

def cooking_time(url):
    soup = parse(url)
    time_div = soup.select('div[class*="cook-and-prep-time"]')
    times = time_div[0].find_all('li')
    return [[time.text for time in times][0], ' '.join([time.text for time in times][1:])]

def recipe_list(url):
    soup = parse(url)
    for EachPart in soup.select('section[class*="method"]'):
        steps = EachPart.find_all('li')
        steps_clean = [steps[i].find('p').text for i in range(len(steps))]
    return steps_clean
        
        

def recipe_name(url):
    return ' '.join(url.split('recipes/',1)[1].split('-'))


def compile_recipe(url):
    return {'url':url, 'name':recipe_name(url), 'instructions':recipe_list(url), \
            'ingredients':ingredient_list(url), 'times':cooking_time(url)}



