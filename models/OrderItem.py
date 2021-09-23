
#OrderItem.py module

from random import randint


class OrderItem:
    
    
    def __init__( self, _id, _itemId, _quantity ):
       
        if _id in range( 0, 1_000_000 + 1 ):
            self.setId( _id )
        
#        if _id == None:
#            raise TypeError( "ID must be of type int" )
        
        else:
            print( f"ID = {_id}" )
            input("for continue press Enter")
#            raise ValueError( "id out of range" )

        self.setItemId( _itemId )
        self.setQuantity( _quantity )
    

    def setId( self, id ):
        self._id = id
    
    def getId( self, id ):
        return self._id


    def setItemId( self, itemId ):
        self._itemId = itemId

    
    def getItemId( self, itemId ):
        return self._itemId

    
    
    def setQuantity( self, quantity ):
        if quantity <= 0:
            raise ValueError( "Quantity can't be 0 or negative!" )
        
        self._quantity = quantity

    
    def getQuantity( self, quantity ):
        return self._quantity

    
    
    def __str__(self):
        return f" item: {self._id:6}; itemId: {self._itemId:12} X {self._quantity}"

    def __repr__ ( self ):
        return self.__str__()

class OrderItemRepositoryFactory:

#FACTORY METHODS ####################
    
    def __init__( self ):
        self._lastCreatedId = 0
        self._orderItems = []

    def getOrderItem( self, itemId, quantity ):
        obj = OrderItem( id, itemId, quantity )
        self._lastCreatedId += 1
        obj._id = self._lastCreatedId

	#remember the obj ref in the list
        self.save( obj )
        return obj  


#REPOSITORY METHODS ####################

    def save( self, orderItem ):

        if orderItem in self._orderItems:
            raise ValueError( "The same item is already in list!" )
        
        self._orderItems.append( orderItem )


    def all( self ):
        return tuple(self._orderItems)

    def findById( self, id ):
        for i in self._orderItems:
            if( i._id == id ):
                return i
        return None        

    def deleteByItemld( self, id ):
        for i in self._orderItems:
            if( i._id == id ):
                self._orderItems.remove(i)
        return None        




