from zaifapi import *
import urllib.request, json
import datetime
import os

def exe(event, context):
    zaif = ZaifPublicApi()
    mona_price = zaif.last_price('mona_jpy')['last_price']
    pepe_price = zaif.last_price('pepecash_jpy')['last_price']
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
    now = now.strftime("%Y/%m/%d %H:%M:%S")
    url = os.getenv("WEBHOOK_URL", "")
    method = "POST"
    headers = {"Content-Type" : "application/json"}
    obj = {"value1" : mona_price, "value2" : pepe_price, "value3" : str(now)} 
    json_data = json.dumps(obj).encode("utf-8")
        
    request = urllib.request.Request(url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")
