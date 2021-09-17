#!/usr/bin/env python3


from boot import *
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
        prf.saveAll( tds.getTestProducts() )
        printItems( "Catalog of products", prf.all() )
        answer = input( "\nAdd to cart? (type y or n)\n >>> " )
        
        if answer == "y":
            #product search logic
            productId = int(input( "enter product id: >>>  " ))
            product = prf.findById( productId )

            if product != None:
                quantity = int(input(f"How many \"{product.name}\" do you want? "))
                

                #add to cart logic
                clientId = int( input( "Enter your client ID\n >>> " ))
                order = orf.findByCustomerId( clientId )
                
                if order == None:
                    order = orf.getOrder( [], 0, clientId, 0 ) 
                
                orderItem = oirf.getOrderItem( product.id, quantity )
                order.addItem( orderItem._id )
                print(order)
                print(orderItem._itemId )
            else:
                system( "clear" )
                print("\nYou entered missing code. Try again.")
        else:
            print( "ok" )

    
    if option == 2:
        pass
    
    if option == 0:
        print( "Thank you for using our app\n" )
        break
    
