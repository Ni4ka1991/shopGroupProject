

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
    


def OrderItemRepositoryFactory( start, name ):
    lastCreatedId = [start]
    new_obj = OrderItem( lastCreatedId[0] + 1, name )
    lastCreatedId.append( start + 1 )
    print(lastCreatedId)
    input("hit enter")
    return new_obj

def doManyObj( lastCreatedId[-1], start, end ):
    for i in range( start, end):
        return OrderItemRepositoryFactory( lastCreatedId[-1], "Soup" )











