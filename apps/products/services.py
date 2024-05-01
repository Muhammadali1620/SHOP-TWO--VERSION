import requests

def get_usd_price():
   url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/'
   response = requests.get(url=url)
   return float(response.json()[0]['Rate'])