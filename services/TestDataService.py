import requests 

class TestDataService:
    
    def getTestProducts( self, count = 20 ):
        res = requests.get("https://fakestoreapi.com/products")
        data = res.json()
        print(data)
#        else:
#            raise Exeption( "Connection error!" )
       
        return []


