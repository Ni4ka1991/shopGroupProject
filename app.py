#!/usr/bin/env python3


from boot import *
from models.OrderItem import *
from os import system
from services.TestDataService import *
from models.Money import *
from models.Product import *
from models.Currency import *
from ui.index import *
from random import randrange


system ("clear")

while True:

    option = printOptions( "e-SHOP", MAIN_MENU ) #>>>> HW: need to do the check if printOption < max and > min
    
    if option == 1:

        
#        prf.save( tds.getTestProducts( 2 ) )


#        prf.getProduct( tds.createTestProducts( "testProducts" ), Money( 6789905, "MDL" ) )
        prf.save( prf.getProduct( tds.createTestProducts( "testProducts" ), Money( 205, "USD" ) ) )
#        prf.save( prf.getProduct( tds.createTestProducts( "testProducts" ), Money( 2536708, "MDL" ) ) )


        printItems( "Catalog of products", prf.all() )
        answer = input( "\nAdd to cart? (type y or n)\n >>> " )
        
        if answer == "y":
            #product search logic
            productId = int( input( "Enter product id: >>>  " ))
            product = prf.findById( productId )

            if product != None:
                quantity = int( input( f"How many \"{product._name}\" do you want? " ))
                

                #add to cart logic
                clientId = int( input( "Enter your client ID\n >>> " )) #13
                order = orf.findByCustomerId( clientId ) # orderRepositoryFactory.findByCustomerId( 13 )
#                print( f"if client with id {clientId} exist? {order}" ) #-> None
#                input( "hit Enter " )
                if order == None: 
                    order = orf.getOrder( [], 0, clientId, 0 ) #get a NEW order( [itemList], totalCost, customerId, paymentId )
#                input( "hit Enter " ) --- debugged up to this point
#                oi = OrderItem( 123456, product._id, quantity ) # here control passed to module OrderItem.py -> crete object oi with _id = 123456
#                print( oi._id )
#                input( "control from module app.py hit Enter " ) # --- debugged. 
                orderItem = oirf.getOrderItem( product._id, quantity )
#                print( f"{orderItem}" )
#                input( "hit Enter " )

                order.addItem( orderItem._id )
                system( "clear" )
                print( "Here you can see your order information:\n" )
                print( f"Customer nr. < { clientId } > ordered:" )
                print( order )
                print( orderItem )
#                print( f" You ordered item with ID: { orderItem._itemId }" )
#                print( f" Quantity: { orderItem._quantity }" )
                print( "#" * 14 )
                    
            else:
                system( "clear" )
                print( "\nYou entered missing code. Try again." )
        else:
            print( "ok" )

    
    if option == 2:
        pass
    
    if option == 0:
        system( "clear" )
        print( "Thank you for using our app\n" )
        break
   














 
