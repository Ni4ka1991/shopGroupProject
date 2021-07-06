

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

#FACTORY METHODS ####################
    
    def __init__( self ):
        self.lastCreatedId = 0
        self.orderItems = []

    def getOrderItem( self, itemld, quantity ):
        obj = OrderItem( id, itemld, quantity )
        self.lastCreatedId += 1
        obj.id = self.lastCreatedId

	#remember the obj ref in the list
        self.save( obj )
        return obj  


#REPOSITORY METHODS ####################

    def save( self, orderItem ):
        self.orderItems.append( orderItem )


    def all( self ):
        return self.orderItems


