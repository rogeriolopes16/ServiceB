import pika
from modules.setS3 import *

# funtion que pega notificações na fila do RabbitMQ
def getRabbit():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, '/',credentials))
    channel = connection.channel()

    channel.queue_declare(queue='ServiceA')

    def callback(ch, method, properties, body):
        print("Notificação recebida %r" % body)
        setS3(body) # chama funtion para envio ao S3

    channel.basic_consume(queue='ServiceA', on_message_callback=callback, auto_ack=True)

    print('Agurdando por mensagens.')
    channel.start_consuming()
