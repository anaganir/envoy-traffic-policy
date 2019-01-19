#!/usr/bin/python
# -*- coding: utf-8 -*-
# App copied from https://docs.docker.com/get-started/part2/
import sys
from flask import Flask, abort
import os
import requests

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello():
    #r = requests.get('http://240.10.0.2:4321/')
    r = requests.get('http://240.10.0.10:1234/retry')
    print(r.text)
    return r.text
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))

