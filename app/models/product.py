from app.models.opinion import Opinion
from app.utils import extractComponent
from app.models.opinion import Opinion
import json

class Product:
    def __init__(self, productId, productName = None, opinions = []):
        self.productId = productId
        self.productName = productName
        self.opinions = opinions

def extraProduct(self):
    
    respons = requests.get('https://www.ceneo.pl/{}#tab=reviews'.format(self.productId))
    page = 2
    while respons:
        print(page)
        pageDOM = BeautifulSoup(respons.text, 'html.parser')
        opinions = pageDOM.select("div.js_product-review")
        for opinion in opinions:
            self.opinions.append(Opinion().extractOpinion())
        respons = requests.get(
            'https://www.ceneo.pl/{}/opinie-'.format(self.productId)+str(page), allow_redirects = False)
        if respons.status_code==200:
            page += 1
        else:
            break
    def extractProduct(self):
        with open(f"./opinions/{self.productId}.json", "w", encoding="UTF-8") as f:
            json.dump(opinionsList, f, indent=4, ensure_ascii=False)

    def __dict__(self):
        pass

     def __str__(self) -> str:
        pass