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

tds = TestDataService()
dic = tds.createTestProducts()
print(dic)











 
