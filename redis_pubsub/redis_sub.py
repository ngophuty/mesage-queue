import redis

r = redis.Redis(host='localhost', port=6379, db=0)

pubsub = r.pubsub()

pubsub.subscribe('channel-1','channel-2')

for message in pubsub.listen():
    if message['type'] == 'message':
        print(message['channel'], message['data'])