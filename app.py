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
            productId = int( input( "Enter product id: >>>  " ))
            product = prf.findById( productId )

            if product != None:
                quantity = int( input( f"How many \"{product._name}\" do you want? " ))
                

                #add to cart logic
                clientId = int( input( "Enter your client ID\n >>> " )) #13
                order = orf.findByCustomerId( clientId ) # orderRepositoryFactory.findByCustomerId( 13 )
                
                if order == None: 
                    order = orf.getOrder( [], 0, clientId, 0 ) #get a NEW order( [itemList], totalCost, customerId, paymentId )
<<<<<<< HEAD
                    orderItem = oirf.getOrderItem( product._id, quantity )
                    order.addItem( orderItem._id )
                    system( "clear" )
                    print( " Here you can see your order information vvv" )
                    print(order)
                    print(orderItem._itemId )
                    print( "#" * 14 )
                else:
#                    
                   orderItem = oirf.getOrderItem( product._id, quantity )
#                    order.addItem( orderItem._id )
                    print( f"Customer nr. <{clientId}> ordered --> {lastOrder} " )
                    print( f"You ordered item with ID: { orderItem._itemId}" )
=======
                orderItem = oirf.getOrderItem( product._id, quantity )
                order.addItem( orderItem._id )
                system( "clear" )
                print( "Here you can see your order information:\n" )
                print( f"Customer nr. < { clientId } > ordered:" )
                print( order )
                print( orderItem )
#                print( f" You ordered item with ID: { orderItem._itemId }" )
#                print( f" Quantity: { orderItem._quantity }" )
                print( "#" * 14 )
>>>>>>> edade528549a4f606fb17bfa47a4413d431d1094
                    
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
    
