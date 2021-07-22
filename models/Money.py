class Money:

    def __init__( self,  amount, currency ):
        self.amount = amount
        self.currency = currency

    def __str__( self ):
        return f"\n "\
               f"amount:   {self.amount}\n "\
               f"currency: {self.currency}\n "
    
    def __repr__( self ):
        return str( self )
