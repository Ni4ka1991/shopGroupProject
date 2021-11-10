from random import randint
from random import randrange
import json
import requests 
from models.Product import Product
from models.Money import Money

test_var = 123
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
                name = item[ "title" ]
                external_id = item[ "id" ]
                price = item[ "price" ]
#                product = Product( 000, item["title"], Money( item["price"], "USD" ), item["id"])
#                products.append(product)
#                return product
            ##### Transformer ###########################            

        else:
            raise Exeption( "Connection error!" )
       
#        return product

    def createTestProducts( self, fileName ):

        ## load data #######
        file = open( f"./data/{fileName}.json", "r" )
        data = json.loads( file.read() )
        ## load data #######

        ## make a random combination of lists ###
        def combinator( data ):
            ### readable view ####
            companies = data.get( 'company')
            models    = data.get( 'model' )
            series    = data.get( 'series' )
            ### readable view ####
            
            ### combinator ###
            prod = companies[ randint( 0, ( len( companies )  - 1 ) ) ] + " " +\
                   models   [ randint( 0, ( len( models ) - 1 ) ) ] + " " +\
                   series   [ randint( 0, ( len( series ) - 1 ) ) ] +\
                   str( randint( 201, 1034 ))
            return prod     
            ### combinator ###
            
        return combinator( data )

