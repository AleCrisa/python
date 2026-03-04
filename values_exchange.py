
import requests
from dotenv import load_dotenv 

import os
load_dotenv('.env')
API_KEY = os.getenv('CUR_API_KEY')
#API_KEY ='d646905359ff48a863165f5d'

first_cur = input("Inserisci la prima valuta: ").upper()
second_cur = input("Inserisci la seconda valuta: ").upper()
amount = int(input("Inserisci il valore: "))

r = requests.get(f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{first_cur}/{second_cur}/{amount}")
rjson = r.json()

if rjson.get('result') == 'error':
    print(f"L'API ha restituito un errore: {rjson.get('error-type')}")
else:
    print(f'{amount} {first_cur} sono {rjson["conversion_result"]:.2f} in {second_cur}')