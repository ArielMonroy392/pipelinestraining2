import time
import os
import redis
from flask import Flask

app = Flask(__name__)
redis_port = int(os.environ.get('REDIS_PORT', 6379))
print(f"Using Redis port: {redis_port}")
cache = redis.Redis(host='redisService', port=redis_port)

def get_hit_count():
    retries = 10
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries = retries - 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)