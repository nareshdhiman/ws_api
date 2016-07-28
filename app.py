import socket
from os import getenv
import redis

from flask import Flask, jsonify, g, abort


app = Flask(__name__)
app.config.update(dict(
    DEBUG=True,
    REDIS_HOST='redis',
    REDIS_PORT='6379'
))
app.config.from_envvar('APP_SETTINGS', silent=True)

def init_db():
    if not hasattr(g, 'redis'):
        g.redis =  redis.StrictRedis(db=0, host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])
    return g.redis

@app.route("/")
def index():
    return "hello world"

@app.route("/key/<key>")
def key(key):
    r = init_db()
    return jsonify(counter=r.incr(key))

@app.route("/_healthcheck")
def healthcheck():
    ok = init_db().ping()
    if not ok:
        abort(500)
    return "OK", 200


@app.route("/_reset", methods=["POST"])
def reset():
    r = init_db()
    r.flushdb()
    return "", 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
