#!/usr/bin/env python3

from models.OrderItem import *
from os import system
from services.TestDataService import *
from models.Money import *
from models.Product import *
from models.Currency import *
#Make a factory

orf = OrderItemRepositoryFactory()

#Create some products

"""
multistrring
comments

"""
#view

system ("clear")

#service initialization
cs = CurrencyService()
#######################

curency = cs.getCurrencies()
print(curency)
