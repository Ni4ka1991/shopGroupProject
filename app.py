#!/usr/bin/env python3

from models.OrderItem import *
from os import system


def doIt( start, end ):
    for i in range( start, end +1 ):
        a = getSomething( i, "Soup", 35 )

system ("clear")

print(doIt(0,10))


