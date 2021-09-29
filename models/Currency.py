# Currency.py module

class Currency:
    
    def __init__(self, _id, _code, _nominal, rate ):
        
        self.setId     ( _id )
        self.setCode   ( _code )
        self.setNominal( _nominal )
        self.setRate   ( _rate )

# set get methods

    def setId( self, id ):
        self._id = id
    
    def getId(self, id ):
        return self._id
    
    def setCode( self, code ):
        self._code = code
    
    def getCode( self, code ):
        return self._code
    
    def setNominal( self, nominal ):
        self._nominal = nominal
    
    def getNominal( self, nominal ):
        return self._nominal
    
    def setRate( self, rate ):
        self._rate = rate
    
    def getRate( self, rate ):
        return self._rate
####    
    
    def __str__( self ):
        return f"\n "\
        f"id:      {self._id}\n"\
        f"code:    {self._code}\n"\
        f"nominal: {self._nominal}\n"\
        f"rate:    {self._rate}"
    
    def __repr__( self ):
        return self.__str__()   
   
