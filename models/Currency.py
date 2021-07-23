import requests
from datetime import date

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
        res = requests.get(f"https://www.bnm.md/ru/official_exchange_rates?get_xml=1&date={today}")
        
        if res.status_code == 200:
            print("We get it!!!")
        else:
            raise Exception( "Connection Error!" )
