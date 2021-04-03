######################################################### https://t.me/TITANHACKY #########################################################


import requests
import json
import config
from Messages import Messages
from CallBackQuery import CallBackQuery

#Getting Url
def getUpdates(offset=None):
    url = f"{config.BotToken()}/getUpdates?timeout=100000000000000000000000"
    if offset:
        url = url+f"&offset={offset+1}"
    r=requests.get(url)
    return json.loads(r.content)

#Getting Updates
def Updates():
    updateId = None
    while True:
        Updates1(updateId)

#New Function For Updates
def Updates1(updateId):
    updates = getUpdates(offset=updateId)
    result = updates["result"]
    if result:
        for result in result:
            updateId = result["update_id"]
            Messages(result)
            CallBackQuery(result)
            Updates1(updateId)

if __name__ == '__main__':
    Updates()

######################################################### https://t.me/TITANHACKY #########################################################