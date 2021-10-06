
import requests
import datetime
import xml.etree.ElementTree as ET
from os import system
from urllib import request

class CurrencyService:
    
    def getCurrencies( self, count = 20 ):

        ### get a usable format of date ## 
        date = datetime.datetime.now()
        today = date.strftime( "%d.%m.%Y" )
        ###____________________________ ## 
        
        print( "waiting for server response ..." )
        url = f"https://www.bnm.md/ru/official_exchange_rates?get_xml=1&date={today}"
        res = requests.get( url )
        currencies = []

        if res.status_code == 200:
            input( "hit Enter" )
            data = res.text
#            tree = ET.parse( data )
#            ET.dump( tree )
            root = ET.fromstring( data )
#            system( "clear" )
            print( "#" * 22 ) 
            official_exchange_rate = {}
            for elem in root.findall( "./Valute/" ):
                print( type( elem.tag ))
                print(elem.text)
                official_exchange_rate["{elem.tag}"] = "{elem.text}
                print( official_exchange_rate )
                input("hit Enter ...")
 
        else:
            raise Exception( "Connection Error!" )

        return currencies
