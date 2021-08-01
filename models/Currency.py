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
    
    def getCurrencies( self, count = 20 ):
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
            doc_tree = []
            
            for elem in root.findall("./Valute[@ID='47']/"):
                doc_tree.append(elem.tag)

            
            for i in range( 0, 3 ):
                valute_objs.append(\
                        Currency(\
                        (root.findall(f"./Valute/{doc_tree[0]}"))[i].text,\
                        (root.findall(f"./Valute/{doc_tree[1]}"))[i].text,\
                        (root.findall(f"./Valute/{doc_tree[2]}"))[i].text,\
                        (root.findall(f"./Valute/{doc_tree[4]}"))[i].text)\
                                )
            print(valute_objs)
   
        else:
            raise Exception( "Connection Error!" )

        return valute_objs


