import redis

pool = redis.ConnectionPool(host='localhost', port=6379)
r = redis.Redis(connection_pool=pool)
with open('2.txt', 'r+') as f:
    for line in f.readlines():
        line = line.rstrip()
        r.rpush('yanzhenma', ( % s), [line])
