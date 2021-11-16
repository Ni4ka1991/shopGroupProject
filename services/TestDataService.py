from random import randint
from random import randrange
import json
import os
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

            data = res.json()                                  # save load data in var "data"

            for item in data:
                item[ "external_id" ] = item["id"]              #create a new key external_id with value of id or in one line ->>> item["external_id"] = item.pop("id")
                item.pop( "id" )                                #delite key "id"  and his value
                item["name"] = item.pop("title")
                item.pop( "description" )
                item.pop( "category" )
                item.pop( "rating" )
                item.pop( "image" )
            return data

            file_name = "external_items.json"                  # create a var file_name with type str
            full_file = os.path.join( "data", file_name )      # create a var full_file, that concatenates path components data-directory and file_name-var 
            
            if( os.path.isfile( full_file ) == True ):
                os.remove( full_file )

            bu-bu-bu = { "a":1,"b":2 }
            with open( full_file, "w" ) as outfile:
                json.dump( bu-bu-bu, outfile )


        else:
            raise Exeption( "Connection error!" )


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

