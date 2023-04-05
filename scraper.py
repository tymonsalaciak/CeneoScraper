import requests
from bs4 import BeautifulSoup


#product_code = input("Podaj kod produktu: ")
product_code = 96693065
url = f"https://www.ceneo.pl/{product_code}#tab=reviews_scroll"
response = requests.get(url)
page_dom = BeautifulSoup(response.text, "html.parser") # dwa argumenty
opinions = page_dom.select("div.js_product-review") # . odpowiada za class
all_opinions = []
for opinion in opinions:
    single_opion = {
        "oinion_id": opinion["data-entry-id"],
        "author": opinion.select_one("span.user-post__author-name").text.strip(),
        "recommendation": opinion.select_one("span.user-post__author-recomendation > em").text.strip(),
        "rating": opinion.select_one("user-post__score-count").text.strip(),
        "verafied": opinion.select_one("div.review-pz").text.strip(),
        "post_date": opinion.select_one("span.user-post__published > time:nth-child(1)")["datetime"].strip(),
        "purchase_date": opinion.select_one("span.user-post__published > time:nth-child(2)")["datetime"].strip(),
        "vote_up": opinion.select_one("buton.vote-yes")["data-total-vote"].strip(),
        "vote_down": opinion.select_one("buton.vote-no")["data-total-vote"].strip(),
        "content": opinion.select_one("div.user-post__text").text.strip(),
        "cons": [cons.text.strip() for cons in  opinion.select_one("div.review-feature__title--negatives~div.review-feature__item")],
        "pros": [pros.text.strip() for pros in  opinion.select_one("div.review-feature__title--positives~div.review-feature__item")],

    }
    print(type(opinions))
#print(page_dom.prettify()) # .text .status_code response.text
#[cons.text.strip() for cons in  opinion.select_one("div.review-feature__title--negatives~div.review-feature__item") ]
all_opinions.append(single_opion)
print(all_opinions)



