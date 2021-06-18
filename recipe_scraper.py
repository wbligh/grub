





"""
        Recipe Web Scraper
           
"""

import requests
from bs4 import BeautifulSoup

url = "https://understat.com/league/EPL"

headers = requests.utils.default_headers()  # a bunch of default headers
headers.update({  # add another one to the default set we just created
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',  # firefox v52 useragent
})  # this makes the site thing we're on ubuntu running firefox

results = requests.get(url, headers=headers)

soup = BeautifulSoup(results.text, "html.parser")