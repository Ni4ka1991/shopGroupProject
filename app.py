#!/usr/bin/env python3

from models.OrderItem import *
from os import system

#Make a factory

orf = OrderItemRepositoryFactory()

#Create some products

oi1 = orf.getOrderItem( "ZNATOK", 300 )
oi2 = orf.getOrderItem( "DOLL",   450 )


#view

system ("clear")
print(oi1)
print(oi2)
