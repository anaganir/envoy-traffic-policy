#!/usr/bin/python
# -*- coding: utf-8 -*-
# App copied from https://docs.docker.com/get-started/part2/
import sys
from flask import Flask, abort
import os
import time
import requests

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello():
    if(os.getenv('SLEEP')):
        print('sleep seconds...' + os.getenv('SLEEP'))
        time.sleep(float(os.getenv('SLEEP')))
    print('request...')
    # Using envoy's address to communicate to the S2
    r = requests.get('http://240.10.0.10:1234/retry')
    print(r.text)
    return r.text
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))

