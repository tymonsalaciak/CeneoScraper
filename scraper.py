import requests
from bs4 import BeautifulSoup


#product_code = input("Podaj kod produktu: ")
product_code = 96693065
url = f"https://www.ceneo.pl/{product_code}#tab=reviews_scroll"
response = requests.get(url)
peage_dom = BeautifulSoup(response.text, "html.parser") # dwa argumenty

print(peage_dom.prettify()) # .text .status_code response.text
