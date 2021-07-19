#!/usr/bin/env python3

from models.OrderItem import *
from os import system

#Make a factory

orf = OrderItemRepositoryFactory()

#Create some products

oi1 = orf.getOrderItem( "ZNATOK", 300 )
oi2 = orf.getOrderItem( "DOLL",   450 )
oi3 = orf.getOrderItem( "CAR",    1150 )


#view

system ("clear")

orf.save( "SPIDERMAN", 12 )
print(orf.all())

