import socket
import os
import redis

from flask import Flask, jsonify


MAIN_KEY="main"
app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return jsonify(counter=r.incr(MAIN_KEY))


if __name__ == "__main__":
    host = socket.gethostbyname("mrredis.mesos")
    print "is redis host: ", host
    r = redis.StrictRedis(host=host, port=5656, db=0)
    print r.get(MAIN_KEY)
    app.run(host="0.0.0.0", port=5002)
