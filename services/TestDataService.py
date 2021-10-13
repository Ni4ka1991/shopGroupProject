from random import randint
from random import randrange
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
                   series   [ randint( 0, ( len( series ) - 1 ) ) ] + " " +\
                   str( randint( 201, 1034 ))
            return prod     
            ### combinator ###

        ## make a required count of products ###
        for i in range( 0, count ):        
            products.append( Product( 2, combinator( data ), Money( randrange( 4_000, 24_001, 100 ), "MDL ") ))
        ## make a required count of products ###
        return products

