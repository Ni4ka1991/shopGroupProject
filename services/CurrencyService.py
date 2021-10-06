
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
            official_exchange_rate = {}
            my_list = []
            for elm in root.findall( "./"):
                 my_list.append( elm.attrib )
            print( my_list )

            for elem in root.findall( "./Valute/" ):
                print( f"{elem.tag} - {elem.text}" )
                official_exchange_rate[elem.tag] = elem.text
                print( official_exchange_rate )
                input( "hit Enter" )
             
        else:
            raise Exception( "Connection Error!" )

        return currencies
