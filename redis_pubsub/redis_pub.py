import redis

r = redis.Redis(host="localhost", port=6379, db=0)

for i in range(10):
    message = f"this is message {i}"
    r.publish('channel-1',message=message)