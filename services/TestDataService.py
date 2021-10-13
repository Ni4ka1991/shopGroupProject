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

    def createTestProducts( self, fileName, count = 20 ):

        products = []

        file = open( f"./data/{fileName}.json", "r" )
        data = json.loads( file.read() )


        def combinator( data ):
            companies = data.get( 'company')
            models    = data.get( 'model' )
            series    = data.get( 'series' )

#            prod = companies[ randint( 1, 6 ) ] + " " +\
#                   models   [ randint( 1, 5 ) ] + " " +\
#                   series   [ randint( 1, 8 ) ] +\
#                   str( randint( 201, 1034 ))
#            return prod     

            prod = companies[ randint( 0, ( len( companies )  - 1 ) ) ] + " " +\
                   models   [1] + " " +\
                   series   [2] +\
                   str( randint( 201, 1034 ))
            return prod     


#        for i in range( 0, 20 ):        
        products.append( combinator( data ) )
        products.append( combinator( data ) )
        products.append( combinator( data ) )
        products.append( combinator( data ) )
        products.append( combinator( data ) )
        products.append( combinator( data ) )
        products.append( combinator( data ) )
        products.append( combinator( data ) )
        products.append( combinator( data ) )
        products.append( combinator( data ) )
        products.append( combinator( data ) )
        products.append( combinator( data ) )


        return products

