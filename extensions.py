import requests
import json
from config import keys, API_KEI

class ConvetrionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
   
        if quote == base:
            raise ConvetrionException(f'Не удалось перевести одинаковые валюты {base}')
        
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvetrionException(f'Не удалось обработать валюту {quote}')
        
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvetrionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConnectionError (f'Не удалось обработать количество {amount}')
        
        pair = base_ticker + quote_ticker

        r = requests.get(f'https://currate.ru/api/?get=rates&pairs={pair}&key={API_KEI}')
        total_base = round(float(json.loads(r.content)['data'][pair]) * amount,5)
    
        return total_base
    

def main(): #тестирование API от currate.ru на паре USD RUB

    print("Test 100 USD -> RUB = ", CryptoConverter.get_price(quote = 'рубль', base = 'доллар', amount = '100'))

if __name__ == "__main__":
    main()