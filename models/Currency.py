import requests
from datetime import date
import xml.etree.ElementTree as ET
import os

class Currency:
    
    def __init__(self, id, code, nominal, rate ):
        self.id = id
        self.code = code
        self.nominal = nominal
        self.rate = rate

    def __str__( self ):
        return f"\n "\
        f"id:      {self.id}\n"\
        f"code:    {self.code}\n"\
        f"nominal: {self.nominal}\n"\
        f"rate:    {self.rate}"
    
    def __repr__( self ):
        return self.__str__()   
   


class CurrencyService:
    
    def getCurrencies( self, count = 10 ):
        today = date.today()
        print( "waiting for server response ..." )
        url = "https://www.bnm.md/ru/official_exchange_rates?get_xml=1&date={today}"
        res = requests.get( url, allow_redirects = True )

        if res.status_code == 200:
            file_name = "file.xml"
            full_file = os.path.join( "data", file_name )

            if (os.path.exists( full_file ) == True):
                os.remove( full_file )
            
            open(full_file, "wb").write(res.content)
            root = ET.parse(full_file)
            
            valute_code = root.findall( "Valute/NumCode" )
            valute_code = root.findall( "Valute/NumCode" )
            valute_code = root.findall( "Valute/NumCode" )
            valute_code = root.findall( "Valute/NumCode" )
            
            for 
        else:
            raise Exception( "Connection Error!" )










