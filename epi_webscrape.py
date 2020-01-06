import copy
import pandas as pd

# Requests sends and recieves HTTP requests.
import requests

# Beautiful Soup parses HTML documents in python.
from bs4 import BeautifulSoup


def scrape_epicurious_page(n):
    '''scrape epicurious.com recipes and add to mongo database'''

    search_url = 'https://www.epicurious.com/search/?sort=mostReviewed&page={}'.format(n)
    searchrequests = requests.get(search_url)
    searchsoup = BeautifulSoup(searchrequests.content,'html.parser')

    review_container = searchsoup.find("div", {"class": "results-group"})
    article = review_container.find("article")

    recipe_links=[]
    for row in review_container:
        columns = row.find_all("h4")
        for i in columns:
            for n in i:
                recipe_links.append(n['href'])

    recipe_info_list =[]
    recipe_requests = []
    for link in recipe_links:
        recipe_url = 'https://www.epicurious.com'+link
        recipe_requests.append(requests.get(recipe_url))
        #grabs all links on page and puts into recipe requests list

    soups = []
    for recipe_r in recipe_requests:
        soups.append(BeautifulSoup(recipe_r.content,'html.parser'))
        #parses all pages and adds into soups list

    reviews = []
    for soup in soups:
        recipes = []

        #add rating
        for _ in range(1):
            try:
                rating_container = soup.find("div", {"class": "user-interactions"}) #finding container for rating
                reviews.append(rating_container.find('span')) #find row for rating
                for r_container in reviews:
                    ratingdict = {}
                    ratingdict['Rating'] = r_container.text.strip()[:-2]
            except:
                pass

        #add review count
        for _ in range(1):
            try:
                review_container = soup.find("div", {"class": "review-rating"})
                rows = review_container.find_all("span")
                for row in rows:
                    reviewsdict = {}
                    reviewsdict['Reviews'] = row.text.strip()
            except:
                pass

        #add make it again
        for _ in range(1):
            try:
                make_container = soup.find("div", {"class": "prepare-again-rating"})
                rows = make_container.find_all("span")
                for r in rows:
                    makedict = {}
                    makedict['Make_Again'] = r.text.strip()
            except:
                pass

        #add nutrition info
        nutrition_facts = []
        for _ in range(1):
            try:
                div = soup.find("div", {"class": "nutrition content"})
                list_ = div.find("ul")
                rows = list_.find_all("li")
                empty_row = {}
                for row in rows:
                    new_row = copy.copy(empty_row)
                    columns = row.find_all("span")
                    new_row[columns[0].text.strip()] = (columns[1].text.strip())
                    nutrition_facts.append(new_row)
            except:
                pass

        #add tags
        tag_tags=[]
        for _ in range(1):
            try:
                tag_container = soup.find("div", {"class": "menus-tags content"})
                tag_list = tag_container.find("dl")
                tags = {}

                count = 0
                for row in tag_list:
                    count += 1
                    tags['Tag' +' #{}'.format(count)] = row.text.strip()
                    tag_tags.append(tags)
            except:
                pass


        #add ingredients
        for _ in range(1):
            try:
                div = soup.find("div", {"class": "ingredients-info"})
                list_ = div.find("ul")
                rows = list_.find_all("li")
                ingredients_row = {}

                count = 0
                for row in rows:
                    count += 1
                    ingredients_row['Ingredient'+ ' #{}'.format(count)]= row.text.strip()
            except:
                pass


        recipes.append({'Title': soup.title.text.strip()[:-17]}) #grab title and puts it into recipes list

        recipes.append(ratingdict) #appending rating for each recipe

        recipes.append(reviewsdict) #appending review count for each recipe

        recipes.append(makedict) #appending review count for each recipe

        for i in nutrition_facts: #appending nutritional facts
            recipes.append(i)

        recipes.append(tags)

        recipes.append(ingredients_row)

        recipe_info = {}
        for i in recipes:
            for i,v in i.items():
                if i not in recipe_info.keys():
                    recipe_info[i] = v

        recipe_info_list.append(recipe_info)

    for features in recipe_info_list:
        recipes_table.insert_one(features)
    #     return recipe_info_list


from pymongo import MongoClient
client = MongoClient('localhost', 27017)

# Access/Initiate Database
recipe_db = client.recipe_database

# Access/Initiate Table
recipes_table = recipe_db.recipes_table

for n in range(1,1850):
    scrape_epicurious_page(n)

recipes = recipes_table.find()
recipe_table = pd.DataFrame(list(recipes))
