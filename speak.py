from aip import AipSpeech,AipNlp
import os
import tuling
from uuid import uuid4
""" 你的 APPID AK SK """
APP_ID = '14941552'
API_KEY = '9bkkxrBBL7z2vWZ5tPAVuNbC'
SECRET_KEY = '2qI6FVwTsZwmRUsaB1yV55Q2rMn5Fwtu'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
client_nlp = AipNlp(APP_ID, API_KEY, SECRET_KEY)

def text2audio(text):
    filename = uuid4()
    result = client.synthesis(text,"zh",1,{
        'spd':4,
        'col':5,
        'pid':7,
        'per':4
    })
    if not isinstance(result, dict):
        with open(f'{filename}.mp3', 'wb') as f:
            f.write(result)
        return f"{filename}.mp3"


def audio2text(filePath):
    os.system(f"ffmpeg -y  -i {filePath}  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {filePath}.pcm")
    with open(f"{filePath}.pcm", 'rb') as fp:
        ret = client.asr(fp.read(), 'pcm', 16000, {
            'dev_pid': 1536,
        })
        return ret.get("result")[0]


def my_nlp(text):

    if client_nlp.simnet("你叫什么名字",text).get("score") >= 0.7:
        return text2audio("我的名字叫二狗子儿")

    if client_nlp.simnet("我是你爸爸",text).get("score") >= 0.7:
        return text2audio("你，给，我，滚！")

    else:
        return text2audio(tuling.goto_tuling(text,"whatever"))







