from .Money import *
#from service.TestDataService import *
from .Currency import *
from os import system

#print( test_var )
#input( "hit" )

class Product:
    def __init__( self, _id, _name, _price, _external_id ):
        self.setId( _id )
        self.setName( _name )        
        self.setPrice( _price )
        self.setExternalId ( _external_id )

    def setId( self, id ):
        if type( id ) != int:
            raise TypeError( "Id must be of type int" )
        self._id = id
 
    def getId( self ):
        return self._id

    def setName( self, name ):
        if type( name ) != str:
            raise TypeError( "Name must be of type string" )
        self._name = name

    def getName( self ):
        return self._name

    def setPrice( self, price ):
        if type( price ) != Money:
            raise TypeError( "Price must be of type Money!" )
            
        if price.amount < 0:
            raise ValueError( "Product's price cannot be negative!" )
        self._price = price

    def getPrice( self ):
        return self._price
    
    def setExternalId( self, eid ):
        if type( eid ) != int:
            raise TypeError( "Id must be of type int" )
        self._external_id = eid
 
    def getExternalId( self ):
        return self._external_id
       
    def __str__( self ):
        return f"\n " \
               f"Product ID: {self._id}\n " \
               f"Name:{self._name}\n" \
               f"Price:{self._price}\n"\
               f"External_ID:{self._external_id}\n"
               
                            
    def __repr__( self ):
        return str( self )

class ProductRepositoryFactory:

    def __init__( self ):
        self._lastCreatedId = 0
        self._products = []

    def getProduct( self, name, price ):
        _id = 0
        obj = Product( _id, name, price, 444 )
        self._lastCreatedId += 1
        obj._id = self._lastCreatedId
        self.save( obj )
        return self._products

    def save( self, product ):
        print( f"Look here. Here your var product => {product}" )
        print( f"Here you can see a len of _products => {len( self._products )}" )
        input( "hit enter ... at next step  we will append product to _products" )
        self._products.append( product )
#        print( f"Look here. Here your var product => {product}" )
        print( len( self._products ) )
        input( "hit enter ... " )

    def saveAll( self, products ):
        self._products = products

    def all( self ):
        return tuple( self._products )

    def findById( self, _id ):
        for p in self._products: 
            if p._id == _id:
                return p
