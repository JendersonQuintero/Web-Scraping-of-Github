import requests
from bs4 import BeautifulSoup as bs

# URL de búsqueda
url = "https://github.com/"

# Ingreso del nombre de usuario
user = input("Ingrese el usuario de Github: ")

#Combinación de URL con el usuario
url_user = url + user


page_response = requests.get(url_user, timeout=10)
page_content = bs(page_response.content, "lxml")


user_name = page_content.find("span", {"class":"p-name"}).get_text()
user_repositories = page_content.find("span", {"class":"Counter"}).get_text()
user_img = page_content.find("img", {"alt":"Avatar"})["src"]

print(user_name)
print(user_repositories)
print(user_img)