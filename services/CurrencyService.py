
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
        url = f"https://www.bnm.md/en/official_exchange_rates?get_xml=1&date={today}"
        res = requests.get( url )
        currencies = []

        if res.status_code == 200:
            data = res.text
            root = ET.fromstring( data )
            my_dict = {}

            my_list = []
            for elm in root.findall( "./Valute" ):
                b = {}
                b = elm.attrib
                print( b.values() )
                my_list.append( b.values() )

            print( my_list )
            input( "hit Enter" )

            official_exchange_rate_47 = {}
            for elm in root.findall( "./Valute[@ID='47']/"):
                official_exchange_rate_47[elm.tag] = elm.text
#            print( official_exchange_rate_47 )
            
#            print( "#" * 22 )
#
            official_exchange_rate_44 = {}
            for elm in root.findall( "./Valute[@ID='44']/"):
                official_exchange_rate_44[elm.tag] = elm.text
#            print( official_exchange_rate_44 )

            my_dict["47"] = official_exchange_rate_47

            my_dict["44"] = official_exchange_rate_44
            print(my_dict)



             
        else:
            raise Exception( "Connection Error!" )

        return currencies
