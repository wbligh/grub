

'''
            JSON mediator


'''

import pandas
import recipe_scraper as sc
import json
from pymongo import MongoClient

client = MongoClient('mongodb+srv://dbUser_WB:A8KWLm-Ad_fPC-J@cluster0.xb4rm.mongodb.net/db_grub_recipe?retryWrites=true&w=majority',tls=True)


client.list_database_names()







'''

url = "https://www.bbcgoodfood.com/recipes/oregano-chicken-squash-traybake"
url_2 = 'https://www.bbcgoodfood.com/recipes/sweet-potatoes-red-pepper-halloumi'
url_3 = 'https://www.bbcgoodfood.com/recipes/pepper-steak-with-noodles'
url_4 = 'https://www.bbcgoodfood.com/recipes/pasta-alla-norma'
url_5 = 'https://www.bbcgoodfood.com/recipes/pork-fennel-burgers-fennel-slaw'


recipe = sc.compile_recipe(url)

db = client.get_database('db_grub_recipe')

records = db.cl_GF_recipes

records.find({'url': recipe['url']})

records.insert_one(recipe)

'''