from flask import Flask
from fp.fp import FreeProxy
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    proxy = FreeProxy(country_id=['US','UK'], timeout=1, rand=True, anonym=True, https=True).get()
    var22 = proxy.split('/')
    myList = {'ipPort': var22[2], 'country': 'US', 'type': 'http'}
    jsonString = json.dumps(myList, indent=4)
    return jsonString

if __name__ == '__main__':
    app.run()