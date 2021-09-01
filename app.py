from flask import Flask
from redis import Redis
from redis.sentinel import Sentinel

app = Flask(__name__)
sentinel = Sentinel([('redis-sentinel', 10001)], socket_timeout=0.1)
redis = sentinel.master_for('mymaster', socket_timeout=0.1)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'Hello World! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)


