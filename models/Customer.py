class Customer:
    def __init__(self, id, _firstName, _lastName, _addressId): 
        self.__id = id
        self.setFirstName (_firstName)
        self.setLastName (_lastName)
        self.setAddressId (_addressId)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if id in range(1, 1000000):
            self.__id = id
        else:
            raise ValueError ("Enter a range of values from 1 to 1 000 000")
      
    def setFirstName (self, _firstName):
        if type(_firstName) is str:
            self._firstName = _firstName
        else:
            raise TypeError ("Enter a First Name")

    def setLastName (self, _lastName):
        if type(_lastName) is str:
            self._lastName = _lastName
        else:
            raise TypeError ("Enter a Last Name")
        
    def setAddressId (self, _addressId):
        if type(_addressId) is str:
            self._addressId = _addressId
        else:
            raise TypeError ("Enter a adress ID")
    
    def __str__(self):
        return f"\nID customer: {self.__id}\nFirst name: {self._firstName}\nLast name: {self._lastName} \nAdress Id: {self._addressId}\n"
    
    def __repr__(self):
       return self.__str__()

############### 4 Repositories and Factories ##################

class CustomerRepositoryFactory:
    def __init__ (self):
        self._lastCreatedId = 0
        self._customers = []

############### Factory Method ####################

    def getCustomer(self, _firstName, _lastName, _addressId): 
        obj = Customer(id, _firstName, _lastName, _addressId) 
        self._lastCreatedId += 1
        obj.id = self._lastCreatedId

        # remember the obj ref in the list
        self.save(obj)
        return obj
        
############### Reposytory Method #################

    # BREAD -> Browse, Read, Edit, Add, Delete

    def save(self, customer):
        self._customers.append(customer)

    def all(self):
        return tuple(self._customers)

    def findById(self, id):
        for c in self._customers:
            if c.id == id:
                return c
            
    def deleteById(self, id):
        for customer in self._customers:
            if customer.id == id:
                self._customers.remove(customer)
