from bs4 import  BeautifulSoup
import requests
def get_recipe_links_by_page_url(page_url):
    url = page_url
    page = requests.get(url)


    soup = BeautifulSoup(page.content, "html.parser")
    recipeslinks = soup.find_all("a", class_="recipe-card-link")
    recipe_links = []
    for link in recipeslinks:
        recipe_links.append(link["href"])
    
    return recipe_links



my_url = "https://www.marmiton.org/recettes/index/categorie/plat-principal/300?rcp=0"

print(get_recipe_links_by_page_url(my_url))
