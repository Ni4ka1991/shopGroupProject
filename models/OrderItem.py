

#OrderItem.py module
from random import randint


class OrderItem:
    
    
    def __init__( self, id, itemld, quantity ):
       
#        if id in range( 0, 1_000_000 + 1 ):
        self.id = id
        
#        else:
#            raise ValueError( "id out of range" )

        self.itemld   = itemld
        self.quantity = quantity


    def __str__(self):
        return f"{self.id:6} -- {self.itemld:12} -- {self.quantity}"

    def __repr__ ( self ):
        return self.__str__()



class OrderItemRepositoryFactory:
    
    def __init__( self ):
        self.lastCreatedId = 0

    def getOrderItem( self, itemld, quantity ):
        obj = OrderItem( id, itemld, quantity )
        self.lastCreatedId += 1
        obj.id = self.lastCreatedId
        return obj  
