import requests
import datetime
import xml.etree.ElementTree as ET
import os
from urllib import request


class CurrencyService:
    
    def getCurrencies( self, count = 20 ):
        date = datetime.datetime.now()
        today = date.strftime("%d.%m.%Y")
        print( "waiting for server response ..." )
        url = f"https://www.bnm.md/ru/official_exchange_rates?get_xml=1&date={today}"
#        res = request.urlopen("https://www.bnm.md/ru/official_exchange_rates?get_xml=1&date={today}")
        res = requests.get( url, allow_redirects = True )
#        print(res.peek())
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

#    def getValue( self, tag, i ):
#        root.findall(f"./Valute/{tag}"))[i].text
            
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
