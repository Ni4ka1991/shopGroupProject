#!/usr/bin/env python3
import boot
from models.OrderItem import *
from os import system
from services.TestDataService import *
from models.Money import *
from models.Product import *
from models.Currency import *
from ui.index import *



system ("clear")

while True:

    option = printOptions( "e-SHOP", MAIN_MENU ) #>>>> HW: need to do the check if printOption < max and > min
    
    if option == 1:
        pass
    if option == 2:
        pass
    
    if option == 0:
        print( "Thank you for using our app" )
        break
    
