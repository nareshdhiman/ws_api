import socket
from os import getenv
import redis

from flask import Flask, jsonify


MAIN_KEY="main"
app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return jsonify(counter=r.incr(MAIN_KEY))


if __name__ == "__main__":
    services = {
        'redis': {
            'host': getenv('REDIS_HOST', 'redis'),
            'port': getenv('REDIS_PORT', '6379'),
        }
    }

    print "is redis host: ", services['redis']
    r = redis.StrictRedis(db=0, **services['redis'])
    print r.get(MAIN_KEY)
    app.run(host="0.0.0.0", port=5002)
