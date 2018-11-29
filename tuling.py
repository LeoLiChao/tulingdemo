from aip import AipSpeech
from aip import AipNlp
import requests
import os
""" 你的 APPID AK SK """
APP_ID = '14941552'
API_KEY = '9bkkxrBBL7z2vWZ5tPAVuNbC'
SECRET_KEY = '2qI6FVwTsZwmRUsaB1yV55Q2rMn5Fwtu'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
client_nlp = AipNlp(APP_ID, API_KEY, SECRET_KEY)

url = 'http://openapi.tuling123.com/openapi/api/v2'

dic = {
	"reqType":0,
    "perception": {
        "inputText": {
            "text": "附近的酒店"
        },
    },
    "userInfo": {
        "apiKey": "9725e9f706884d9fad4cf61bb076772d",
        "userId": "1"
    }
}

def goto_tuling(q,uid):
    dic["perception"]["inputText"]["text"] = q
    dic["userInfo"]["userId"] = uid
    res = requests.post(url,json=dic)
    return res.json()["results"][0]['values']["text"]

