

'''
            JSON mediator


'''


import pandas
import recipe_scraper as sc
import json
from pymongo import MongoClient



client = MongoClient("mongodb+srv://dbUser_WB:A8KWLm-Ad_fPC-J@cluster0.xb4rm.mongodb.net/db_grub_recipe?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE", connect = False)





'''

url_2 = 'https://www.bbcgoodfood.com/recipes/sweet-potatoes-red-pepper-halloumi'
url_3 = 'https://www.bbcgoodfood.com/recipes/pepper-steak-with-noodles'
url_4 = 'https://www.bbcgoodfood.com/recipes/pasta-alla-norma'
url_5 = 'https://www.bbcgoodfood.com/recipes/pork-fennel-burgers-fennel-slaw'

'''

db = client.get_database('db_grub_recipe')
recipe_records = db.cl_GF_recipes
recipe_link_records = db.cl_GF_recipe_links


scraped_links = [d['url'] for d in list(recipe_records.find({},{'_id':False,'url':True}))]
url = recipe_link_records.find_one({'url':{'$nin':scraped_links}},{'_id':False, 'recipe_url':True})['recipe_url']

# Retrieve URL and initialise recipe object
recipe = sc.compile_recipe(url)

recipe_records.insert(recipe)



#   records.insert_one(recipe)



