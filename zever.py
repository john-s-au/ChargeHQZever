import requests
import zeversolarlocal
import asyncio
import json
loop = asyncio.get_event_loop()
def getCurrentPower() -> int:
   address = "<local ip of zever solar here>"
   url= zeversolarlocal.default_url(address)
   try:
    solar_data = loop.run_until_complete(zeversolarlocal.solardata(url))
   except:
    return 0
   else:
    return solar_data.current_power



def sendPower(power: int):
   solarPower = power/1000
   print(solarPower)
   url = "https://api.chargehq.net/api/public/push-solar-data"
   data = {'apiKey':'<siteid here>','siteMeters':{'production_kw':solarPower}}
   headers = {'Content-type': 'application/json','Accept':'text/plain'}
   r = requests.post(url,data=json.dumps(data), headers=headers)
   print(r)



sendPower(getCurrentPower())
