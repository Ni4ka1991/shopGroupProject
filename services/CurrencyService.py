import requests
import datetime
import xml.etree.ElementTree as ET
import os
from urllib import request

class CurrencyService:
    
    def getCurrencies( self, count = 20 ):

        ### get a usable format of date ## 
        date = datetime.datetime.now()
        today = date.strftime("%d.%m.%Y")
        ###____________________________ ## 
        
        print( "waiting for server response ..." )
        url = f"https://www.bnm.md/ru/official_exchange_rates?get_xml=1&date={today}"
        res = requests.get( url )
        data = res.text
        print( data )
        currencies = []

#        if res.status_code == 200:
#            data = res.json()
#            print(data)
              
 
#        else:
#            raise Exception( "Connection Error!" )

        return currencies
