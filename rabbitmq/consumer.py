import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.0.0', port=15672))
channel = connection.channel()

channel.queue_declare(queue="hello")

def callback(channel, method, properties, body):
    print("[x] Received %r" %body)

channel.basic_consume(queue="hello",
                      auto_ack=True,
                      on_message_callback=callback
)

print("[*] wating for message")
channel.start_consuming()