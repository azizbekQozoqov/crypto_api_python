from requests import Request, Session 
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects 
import json 

class Cryptos:
    '''En: This module is a module that makes it easy to work with the CoinMarketCap API. To get acquainted with the module, go to https://github.com/azizbekQozoqov/crypto-api-python GitHub.\nFor information on the API, go to https://coinmarketcap.com/api/documentation/v1. \n\nUz: Bu modul CoinMarketCap API bilan ishlashni osonlashtiradigan moduldir. Modul bilan tanishish uchun https://github.com/azizbekQozoqov/crypto-api-python GitHub saytiga o'ting.\nAPI haqidaa ma'lumot olish uchun https://coinmarketcap.com/api/documentation/v1 saytiga o'ting.'''
    def __init__(self, API_KEY,  LIMIT, CONVERT):
        self.LIMIT = str(LIMIT)
        self.CONVERT = CONVERT
        self.API_KEY = API_KEY

        if not self.API_KEY:
            raise Exception("API KEY is not defined")

        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
	
        parameters = { 'start':'1', 'limit': self.LIMIT, 'convert': self.CONVERT } 
        headers = { 
			'Accepts': 'application/json', 
			'X-CMC_PRO_API_KEY': self.API_KEY
		} 

        session = Session()
        session.headers.update(headers)
	    
        try: 
            response = session.get(url, params=parameters) 
            data = json.loads(response.text)
            self.ALL = data

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            raise e
    # ************************************************************

    def get_all(self):
        return self.ALL["data"]

    def get_by_ID(self, ID):
        if not ID:
            return "ID is not defined."
        else:
            for i in self.ALL["data"]:
                if i["id"] == ID:
                    return i
                else:
                    raise Exception("No equivalent answer was found for the given ID.") 
    
    def get_price_by_ID(self, ID, formated=False):
        if not ID:
            raise Exception("ID is not defined.")
        else:
            for i in self.ALL["data"]:
                if i["id"] == ID:
                    if formated:
                        return "{:,.2f} {}".format(i["quote"][self.CONVERT]["price"], self.CONVERT)
                    else:
                        return i["quote"][self.CONVERT]["price"]
                else:
                    raise Exception("No equivalent answer was found for the given ID.")
    
    def get_list(self):
        with open("./cryp_list.json", "w") as f:
            w = []
            for i in self.ALL["data"]:
                res = {
                    "id" : i["id"],
                    "name" : i["name"],
                    "symbol" : i["symbol"],
                    "slug" : i["slug"],
                    "convert" : self.CONVERT,
                    "price" : i["quote"][self.CONVERT]["price"],
                    "formatted_price" : "{:,.2f} {}".format(i["quote"][self.CONVERT]["price"], self.CONVERT),
                }
                w.append(res)
            return w