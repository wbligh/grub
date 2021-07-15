



'''

BBC Goodfood Directory Scraper

- Hit the recipe query webpage

- Compile URLs and store in JSON collection via Pymongo



'''



import pandas
import recipe_scraper as sc
import json
import random
import requests
import time
from bs4 import BeautifulSoup
from pymongo import MongoClient



# Initialise requests

base_url = 'https://www.bbcgoodfood.com/search/recipes/page/'

sort_url = '?sort=-date'

headers = requests.utils.default_headers()  # a bunch of default headers
headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})  # this makes the site thing we're on ubuntu running firefox



results = requests.get(base_url + '5000' + sort_url , headers=headers)
soup = BeautifulSoup(results.text, "html.parser")


client = MongoClient("mongodb+srv://dbUser_WB:A8KWLm-Ad_fPC-J@cluster0.xb4rm.mongodb.net/db_grub_recipe?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE", connect = False)
db = client.get_database('db_grub_recipe')
records = db.cl_GF_recipe_links


start = time.time()
i = 1

while True:
    print('While Loop interation' + str(i))    
    results = requests.get(base_url + str(i) + sort_url , headers=headers)
    soup = BeautifulSoup(results.text, "html.parser")
    print('Checking break clause')
    try: 
        if soup.select('p[class*="body-copy"]')[0].get_text() == 'Please expand your search criteria':
            break
    except:
        pass
    link_section = soup.select('div[class*="template-search-universal__card"]')
    links = [link.select('a[class*="standard-card-new__article-title"]') for link in link_section]
    for count, link in enumerate(links):
        if records.find_one({'recipe_url': 'https://www.bbcgoodfood.com' + links[count][0]['href']}) is None:
            print('Inserting')
            records.insert_one({'recipe_name' : links[count][0].get_text(), 'recipe_url': 'https://www.bbcgoodfood.com' + links[count][0]['href']})
        else:
            print('URL already in db')
    i+=1
    time.sleep(2+ random.random())






