#!/usr/bin/env python3


from boot import *
from models.OrderItem import *
from os import system
from services.TestDataService import *
from services.CurrencyService import *
from models.Money import *
from models.Product import *
from models.Currency import *
from ui.index import *



system ("clear")

#tds = TestDataService()
#my_prod_list = tds.createTestProducts( "testProducts" )
#print( my_prod_list )

a = prf.getProduct( "bbb", Money( 12, "USD" ) )
print( a ) 








 
