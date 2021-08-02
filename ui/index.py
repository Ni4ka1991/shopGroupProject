

#import
MAIN_MENU = {
    1 : "Catalog",
    2 : "Cart"
}

def printOptions( title,  options ):
    print( f"\n{title}" )
    print( "*" * 30 )
    for key in options:
        print( f"{key}. {options[key]}" )    
    print( "*" * 30 )
    option = int( input (">>  " ))
