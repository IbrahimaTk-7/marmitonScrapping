from bs4 import  BeautifulSoup
import requests
from pprint import pprint


url = "https://www.marmiton.org/recettes/index/categorie/plat-principal/300?rcp=0"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
recipeslinks = soup.find_all("a", class_="recipe-card-link")
recipe_links = []
for link in recipeslinks:
    recipe_links.append(link["href"])

#print(recipe_links[1])

i = 0
while i < len(recipe_links): 
    link_url = recipe_links[i]
    i = i+1
    url = link_url
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    recette_info = soup.find_all("p", class_="RCP__sc-1qnswg8-1 iDYkZP") 

    recipeName = soup.find("h1", class_="SHRD__sc-10plygc-0 itJBWW").text
    duration = str(recette_info[0].text)
    difficultyLevel = recette_info[1].text
    cost = recette_info[2].text

    recipe = {
        'nom': recipeName,
        'durée': duration,
        'niveau': difficultyLevel,
        'cout': cost
    }
    list_recette = []
    list_recette = recipe
    
    print(list_recette)
    