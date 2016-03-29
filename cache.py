import redis

class Cache():
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

    def put(self, key, val):
        self.r.set(key, val)

    def get(self, key):
        return self.r.get(key)
