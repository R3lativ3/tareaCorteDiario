import requests
from datetime import datetime

txt = open("RestultadoCorteDiario.txt", "a")


# * * * * * cd /home/jose/workspace/python && python Corte.py
url = "http://192.168.1.26:3000/api/repartidores/emitirCorte2"
response = requests.get(url)

print(response.text)
print(response.status_code, response.reason)
today = datetime.now()
if response.status_code == 200 :
    txt.writelines("Corte exitoso, msg: "+ response.text +", dia corte: "+ today +" \n" )

if response.status_code == 404 :
    txt.writelines("Sin cuentas en rojo, msg: "+ response.text +", dia corte: "+ today +" \n" )
    

txt.close()