

#import
MAIN_MENU = {
    1 : "Catalog",
    2 : "Cart",
    0 : "Exit"
}



def printOptions( title,  options ):
    print( f"\n{title}" )
    print( "*" * 12 )
    for key in options:
        print( f"{key}. {options[key]}" )    
    print( "*" * 12 )
    option = int( input (">>  " ))

    return option


def printItems( title,  items ):
    print( f"\n{title}" )
    print( "*" * 50 )
    for item in items:
        print( f"{item}" )    
    print( "*" * 50 )
