

#OrderItem.py module



class OrderItem:
    
    
    def __init__( self, _id, itemld, quantity ):
       
        if type(_id) == str:
            
            if _id.isdigit() == True:
                _id = int(_id)
                if _id in range( 1, 1_000_000 + 1 ):
                    self._id       = _id
                else:
                    raise ValueError( "id out of range" )
            else:
                raise TypeError( "id can not be 'str'" )
        if type(_id) == int:
            if _id in range( 1, 1_000_000 + 1 ):
                self.id       = _id
            else:
                raise ValueError( "id out of range" )


        self.itemld   = itemld
        self.quantity = quantity


    def __str__( self ):
        return f"{self.id} -- {self.itemld} -- {self.quantity}"

    def __repr__ ( self ):
        return f"{self.id} -- {self.itemld} -- {self.quantity}"
    

