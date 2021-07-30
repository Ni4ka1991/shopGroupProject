import requests
import datetime
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
        date = datetime.datetime.now()
        today = date.strftime("%d.%m.%Y")
        print( "waiting for server response ..." )
        url = f"https://www.bnm.md/ru/official_exchange_rates?get_xml=1&date={today}"
        res = requests.get( url, allow_redirects = True )

        if res.status_code == 200:
            file_name = "file.xml"
            full_file = os.path.join( "data", file_name )

            if (os.path.exists( full_file ) == True):
                os.remove( full_file )
            
            open(full_file, "wb").write(res.content)
            tree = ET.parse( full_file )
            root = tree.getroot()
            valute_objs = []
            

            valute_NumCode  = root.findall( "Valute/NumCode" )

            valute_CharCode = root.findall( "Valute/CharCode" )
            valute_Nominal  = root.find( "Valute/Nominal" )
            valute_Value    = root.findall( "Valute/Value" )


#            for elem in root.findall("./Valute/"):
#                print(elem.tag, " -- ", elem.text )



            for i in range( 0, 3 ):
                valute_objs.append( Currency( valute_NumCode[i].text, valute_CharCode[i].text, valute_Nominal[i].text, valute_Value[i].text))
            
            print(valute_objs)   
        else:
            raise Exception( "Connection Error!" )

        return valute_objs


