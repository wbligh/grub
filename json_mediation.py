

'''
            JSON mediator


'''


import pandas
import recipe_scraper as sc
import json
from pymongo import MongoClient



client = MongoClient("mongodb+srv://dbUser_WB:A8KWLm-Ad_fPC-J@cluster0.xb4rm.mongodb.net/db_grub_recipe?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE", connect = False)


db = client.get_database('db_grub_recipe')


scraped_links = [d['url'] for d in list(db.cl_GF_recipes.find({},{'_id':False,'url':True}))]
url = db.cl_GF_recipe_links.find_one({'recipe_url':{'$nin':scraped_links}},{'_id':False, 'recipe_url':True})['recipe_url']

# Retrieve URL and initialise recipe object
recipe = sc.compile_recipe(url)

db.cl_GF_recipes.insert_one(recipe)






