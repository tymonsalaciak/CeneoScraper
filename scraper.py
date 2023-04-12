import requests
from bs4 import BeautifulSoup
import json

def extract_tag(ancestor, selector=None, attribiute=None, return_list=False): # none może przyjąc rózne zmienne / false w tym przypadku jest zabiegiem logicznym
    try:
        if return_list:
            return [tag.text.strip() for tag in  ancestor.select(selector)]
        if not selector and attribiute:
            return ancestor[attribiute]
        if attribiute:
            return ancestor.select_one(selector)[attribiute].strip()
        return ancestor.select_one(selector).text.strip()
    except (AttributeError, TypeError):
        return None

#product_code = input("Podaj kod produktu: ")
product_code = 96693065
url = f"https://www.ceneo.pl/{product_code}#tab=reviews_scroll"
response = requests.get(url)
page_dom = BeautifulSoup(response.text, "html.parser") # dwa argumenty
opinions = page_dom.select("div.js_product-review") # . odpowiada za class
all_opinions = []
for opinion in opinions:
    single_opion = {
        "oinion_id": extract_tag(opinion,None ,"data-entry-id"),
        "author": extract_tag(opinion,"span.user-post__author-name"),
        "recommendation": extract_tag(opinion,"span.user-post__author-recomendation > em"),
        "rating": extract_tag(opinion,".user-post__score-count"),
        "verafied": extract_tag(opinion,"div.review-pz"),
        "post_date":  extract_tag(opinion,"span.user-post__published > time:nth-child(1)","datetime"),
        "purchase_date":  extract_tag(opinion,"span.user-post__published > time:nth-child(2)","datetime"),
        "vote_up":  extract_tag(opinion,"button.vote-yes","data-total-vote"),
        "vote_down":  extract_tag(opinion,"button.vote-no","data-total-vote"),
        "content": extract_tag(opinion,"div.user-post__text"),
        "cons": extract_tag(opinion,"div.review-feature__title--negatives~div.review-feature__item", None, True),
        "pros": extract_tag(opinion,"div.review-feature__title--positives~div.review-feature__item", None, True),

    }
    all_opinions.append(single_opion)
with open(f"./opinions/{product_code}.json", "w", encoding="UTF-8") as  jf:
    json.dump(all_opinions, jf, indent=4 , ensure_ascii=False)



    #print(type(opinions))
#print(page_dom.prettify()) # .text .status_code response.text
#[cons.text.strip() for cons in  opinion.select_one("div.review-feature__title--negatives~div.review-feature__item") ]




