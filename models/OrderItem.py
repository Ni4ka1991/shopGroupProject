

#OrderItem.py module



class OrderItem:
    
    
    def __init__( self, id, itemld, quantity ):
       
        if type(id) == str:
            
            if id.isdigit() == True:
                id = int(id)
                if id in range( 1, 1_000_000 + 1 ):
                    print( "Yep" )
                    input("hit ...")
                    self.id       = id
                else:
                    raise ValueError( "id out of range" )
            else:
                raise TypeError( "id can not be 'str'" )
        if type(id) == int:
            if id in range( 1, 1_000_000 + 1 ):
                self.id       = id
            else:
                raise ValueError( "id out of range" )


        self.itemld   = itemld
        self.quantity = quantity


    def __str__( self ):
        return f"{self.id} -- {self.itemld} -- {self.quantity}"

    def __repr__ ( self ):
        return f"{self.id} -- {self.itemld} -- {self.quantity}"
    

