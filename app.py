#!/usr/bin/env python3

from models.OrderItem import OrderItem
from os import system


a = OrderItem( "12", "Soup", 5 )
b = OrderItem( 1_000_000, "Salad", 12 ) 
c = OrderItem( "u", "Salad", 12 )


system ("clear")
print()
print(a)
print(b)
print(c)
b.id = 48
print(b)
b.id = "u"
print(b)
