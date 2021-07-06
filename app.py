#!/usr/bin/env python3

from models.OrderItem import *
from os import system


orf1 = OrderItemRepositoryFactory()

oi1 = orf1.getOrderItem( 43016, "ZNATOK", 300 )

system ("clear")
print(oi1)
