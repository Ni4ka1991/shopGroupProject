

#OrderItem.py module



class OrderItem:
    
    
    def __init__( self, _id, itemld, quantity  = None ):
       
        if _id in range( 1, 1_000_000 + 1 ):
            self.id = _id
        
        else:
            raise ValueError( "id out of range" )

        self.itemld   = itemld
        self.quantity = quantity


    def __str__( self ):
        return f"{self.id} -- {self.itemld} -- {self.quantity}"

    def __repr__ ( self ):
        return f"{self.id} -- {self.itemld} -- {self.quantity}"
    
def OrderItemRepositoryFactory( name ):
    
    lastCreatedId = [0]
    
    obj = OrderItem( lastCreatedId[0] + 1, name, 35 )
    lastCreatedId.append()



