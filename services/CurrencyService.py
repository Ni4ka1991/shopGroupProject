
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

            ### create a list of external Id's #######
            list_of_Id = []
            for elm in root.findall( "./Valute" ):
                d = {}
                d = elm.attrib
                list_of_Id.append( d.get( 'ID' ) )
            ### create a list of external Id's #######
            
            ### get a general dict of vatures sorted by id"
            official_exchange_rate = {}
            for i in list_of_Id:
                dic = {}
                for elm in root.findall( f".Valute[@ID='{i}']/" ):
                    dic[elm.tag] = elm.text
                
                official_exchange_rate[i] = dic
            ### get a general dict of vatures sorted by id"



            for key in official_exchange_rate:
#                print( key )
                print( official_exchange_rate.get( key ) )









             
        else:
            raise Exception( "Connection Error!" )

        return currencies
