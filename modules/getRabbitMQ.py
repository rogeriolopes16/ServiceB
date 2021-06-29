import pika
from modules.setS3 import *

def getRabbit():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, '/',credentials))
    channel = connection.channel()

    channel.queue_declare(queue='ServiceA')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        setS3(body)

    channel.basic_consume(queue='ServiceA', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()