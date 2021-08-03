#executing module

from services.TestDataService import *
from models.Currency import *
from models.Product import *
from models.Order import *
from models.OrderItem import *


#init repos
prf = ProductRepositoryFactory()
orf = OrderRepositoryFactory()
oirf = OrderItemRepositoryFactory()

#init services 
tds = TestDataService()
#c = Currency()


