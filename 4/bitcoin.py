import sys
import requests
import json
import os 
os.system("clear")


try:
    n = float(sys.argv[1])
    if n <= 0:
        raise ValueError()
except IndexError:
    sys.exit("Falta un término.")
except ValueError:
    sys.exit("Valor no válido.")

res = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json',params='bpi:{0}')    

bitcoin_cotizacion_usd = res.json()["bpi"]["USD"]["rate_float"]

print(f"${n * bitcoin_cotizacion_usd:,.4f}")


#API!!! COTIZACION API!!! APIIIIII!!!
#https://api.coindesk.com/v1/bpi/currentprice.json



""" RESPUESTA CON ALL THE JASON
resCompleta = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json',params='bpi:{0}')
print(json.dumps(resCompleta.json(), indent=2))   """