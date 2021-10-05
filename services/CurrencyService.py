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
        currencies = []

        if res.status_code == 200:
            data = res.text
            tree = ET.parse( data )
            root = tree.getroot()

            for i in range( 0, 3 ):
                currencies.append(\
                        Currency(\
                        (root.findall(f"./Valute/{doc_tree[0]}"))[i].text,\
                        (root.findall(f"./Valute/{doc_tree[1]}"))[i].text,\
                        (root.findall(f"./Valute/{doc_tree[2]}"))[i].text,\
                        (root.findall(f"./Valute/{doc_tree[4]}"))[i].text)\
                                )
              
 
        else:
            raise Exception( "Connection Error!" )

        return currencies
