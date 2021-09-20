
# Customer.py module


class Customer:
    def __init__( self, _id, _firstName, _lastName, _addressId ): 
        self.setId( _id )
        self.setFirstName ( _firstName )
        self.setLastName ( _lastName )
        self.setAddressId ( _addressId )

    def setId( self, id ):
        self._id = id    

    def getId( self, id ):
        return self._id

 
    def setFirstName ( self, firstName ):
        if type( firstName ) is str:
            self._firstName = firstName
        else:
            raise TypeError ( "Enter a First Name" ) 

    def setLastName ( self, lastName ):
        if type( lastName ) is str:
            self._lastName = lastName
        else:
            raise TypeError ( "Enter a Last Name" )
        
    def setAddressId ( self, addressId ):
        if type( addressId ) is str:
            self._addressId = addressId
        else:
            raise TypeError ( "Enter a adress ID" )
    
    def __str__( self ):
        return f"\nID customer: {self._id}\nFirst name: {self._firstName}\nLast name: {self._lastName} \nAdress Id: {self._addressId}\n"
    
    def __repr__( self ):
       return self.__str__()

############### 4 Repositories and Factories ##################

class CustomerRepositoryFactory:
    def __init__ (self):
        self._lastCreatedId = 0
        self._customers = []

############### Factory Method ####################

    def getCustomer( self, firstName, lastName, addressId ): 
        obj = Customer( id, firstName, lastName, addressId ) 
        self._lastCreatedId += 1
        obj._id = self._lastCreatedId

        # remember the obj ref in the list
        self.save( obj )
        return obj
        
############### Reposytory Method #################

    # BREAD -> Browse, Read, Edit, Add, Delete

    def save( self, customer ):
        self._customers.append( customer )

    def all( self ):
        return tuple( self._customers )

    def findByCustomerId( self, id ):
        for c in self._customers:
            if c._id == id:
                return c
            
    def deleteByCustomerId( self, id ):
        for customer in self._customers:
            if customer._id == id:
                self._customers.remove( customer )
