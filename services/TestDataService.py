import requests 
from models.Product import Product
from models.Money import Money

class TestDataService:
    
    def getTestProducts( self, count = 20 ):
        print( "waiting for server response ..." )
        res = requests.get(f"https://fakestoreapi.com/products?limit={count}")
        products = []

        data = res.json()
        for item in data:
            product = Product( item["id"], item["title"], Money( item["price"], "USD" ))
            products.append(product)

#        else:
#            raise Exeption( "Connection error!" )
       
        return products


