from flask import Flask,render_template,request,send_file
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from geventwebsocket.websocket import WebSocket

from uuid import uuid4

import speak
import pymongo

client = pymongo.MongoClient(host="127.0.0.1",port="27017")
db = client.text
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ws")
def ws():
    user_socket = request.environ.get("wsgi.websocket") # type:WebSocket
    print(request.environ)
    while 1:
        audio_file = user_socket.receive()
        file_name = uuid4()
        with open(f"{file_name}.wav","wb") as f:
            f.write(audio_file)
        text = speak.audio2text(f"{file_name}.wav")
        filename = speak.my_nlp(text)
        print(text)
        user_socket.send(filename)

@app.route("/get_audio/<filename>")
def get_audio(filename):
    return send_file(filename)


if __name__ == '__main__':
    # app.run("127.0.0.1",6000)
    http_serv = WSGIServer(("0.0.0.0",5000),app,handler_class=WebSocketHandler)
    print(http_serv)
    http_serv.serve_forever()