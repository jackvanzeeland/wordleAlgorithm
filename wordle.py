import pandas as pd
from flask import Flask, request, jsonify, Response
import re
import time
import json
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from io import StringIO, BytesIO

app = Flask(__name__)

@app.route('/')
def hello():
    with open("home.html") as f:
                html = f.read()
    return html
        
@app.route('/letters.html')        
def start():
    f = open("complete_found_in_distribution.html")
    html = f.read()
    f.close
    return html

    
    


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, threaded=False) # don't change this line!

# NOTE: app.run never returns (it runs for ever, unless you kill the process)
# Thus, don't define any functions after the app.run call, because it will
# never get that far.