from bs4 import  BeautifulSoup
import requests
import json
from unicodedata import normalize

def get_recipe_links_by_page_url(page_url):
    url = page_url
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    recipeslinks = soup.find_all("a", class_="recipe-card-link")
    recipe_links = []
    for link in recipeslinks:
        recipe_links.append(link["href"])

    return recipe_links

def get_recipe_info(recipe_url):
    url = recipe_url
    page = requests.get(url)


    soup = BeautifulSoup(page.content, "html.parser")
    recette_info = soup.find_all("p", class_="RCP__sc-1qnswg8-1 iDYkZP") 

    recipeName = soup.find("h1", class_="SHRD__sc-10plygc-0 itJBWW").text
    duration = normalize("NFKD", recette_info[0].text)
    difficultyLevel = recette_info[1].text
    cost = recette_info[2].text

    recipe = {
        'nom': recipeName,
        'durée': duration,
        'niveau': difficultyLevel,
        'cout': cost
    }

    return recipe


my_page_url = "https://www.marmiton.org/recettes/index/categorie/plat-principal/300?rcp=0"
list_recette = get_recipe_links_by_page_url(my_page_url)
list_recette_info = [] 
for recette_link in list_recette:
    recipe_info = get_recipe_info(recette_link)
    list_recette_info.append(recipe_info)

#print(list_recette_info)


with open("data.json", "w" , encoding='utf8') as fp:
    json.dump(list_recette_info, fp, ensure_ascii=False)

with open("data.json", "r") as fp:
    data = json.load(fp)
print(data)
print(type(data))