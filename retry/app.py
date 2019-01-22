#!/usr/bin/python
# -*- coding: utf-8 -*-
# App copied from https://docs.docker.com/get-started/part2/
import sys
import time
from flask import Flask, abort
import time
from redis import Redis, RedisError
import os
import socket

# Connect to Redis

redis = Redis(host='240.10.0.3', port=6379, db=0,
              socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)


@app.route('/retry')
def hello():
    try:
        visits = redis.incr('counter')
        sys.stdout.write("Visit " + str(visits) + "\n")
    except RedisError:
        visits = '<i>cannot connect to Redis, counter disabled</i>'

    if(os.getenv('SLEEP')):
        print('sleep seconds...' + os.getenv('SLEEP'))
        time.sleep(float(os.getenv('SLEEP')))
    
    if os.getenv('STATE', 'Ok') == 'Error' :
        abort(504, {'message':'Force error'})

    html = \
        '<h3>Hello {name}!</h3><b>Hostname:</b> {hostname}<br/><b>Visits:</b> {visits}'
    return html.format(name=os.getenv('NAME', 'world'),
                       hostname=socket.gethostname(), visits=visits)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))

