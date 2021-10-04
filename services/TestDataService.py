
import requests 
from models.Product import Product
from models.Money import Money

class TestDataService:
    
    def getTestProducts( self, count = 20 ):
        print( "waiting for server response ..." )
        res = requests.get(f"https://fakestoreapi.com/products?limit={count}")
        products = []
        
        if res.status_code == 200:
#                                   .json method
#                                     V
            ##### Transformer ( json ---> {list of dictionaries [],[],[] } ---> extaction obj class Products one by one ---> create a list of obj-s #######            

            data = res.json()
            for item in data:
                product = Product( item["id"], item["title"], Money( item["price"], "USD" ))
                products.append(product)

            ##### Transformer ###########################            

        else:
            raise Exeption( "Connection error!" )
       
        return products


