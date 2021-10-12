from random import randint
import json
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

    def createTestProducts( self, fileName ):
        products = {}
        file = open( f"./data/{fileName}.json", "r" )
        data = json.loads( file.read() )

#        company = [ "Samsung", "Nokia", "Apple", "Lenovo", "Huawei", "Motorola" ]
#        model = [ "Galaxy", "Cityman", "Talkman", "Senator", "Actionman", "Vibe", "Phab", "RocStar" ] 
#        series = [ "A", "B", "C", "D", "E", "F", "K", "Z", "W" ]        
        
#        def combinator( ):
#            prod = company[ randint( 0, len( company ) - 1 ) ] + " " +\
#                   model[ randint( 0, len( model ) - 1 ) ] + " " +\
#                   series[ randint( 0, len( series ) - 1 ) ] +\
#                   str( randint( 201, 1034 )) 
#            return prod      
        
#        p =  combinator()
#        return combinator()
        return data

