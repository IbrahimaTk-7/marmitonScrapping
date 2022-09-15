from bs4 import  BeautifulSoup
import requests
from pprint import pprint
def get_recipe_info(recipe_url):
    url = recipe_url
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

    return recipe
###################### Test ###############
my_recipe_url = "https://www.marmiton.org/recettes/recette_boulettes-de-thon_39213.aspx"

print(get_recipe_info(my_recipe_url))


