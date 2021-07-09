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
#print(oi1)
#print(oi2)
#print(oi3)

#print( orf._orderItems )
p = orf.findById(3)
p.setItemld("buka")
p.setQuantity(1)
p.setId(234)
orf.save("buka")
print(orf.all())

#print(f"Method all ---> {orf.all()}")
#print(orf.findById(3))
#print(orf.findById(1))
