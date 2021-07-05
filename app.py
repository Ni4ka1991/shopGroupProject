#!/usr/bin/env python3

from models.OrderItem import *
from os import system


#a = OrderItemRepositoryFactory( 0, "Salad" )
#b = OrderItemRepositoryFactory( 2, "Soup" )

a = doManyObj( 0, 10 )
system ("clear")
print()
print(a)
