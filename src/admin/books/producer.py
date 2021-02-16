import json

import pika

params = pika.URLParameters('amqps://qxbckujb:TNhb9rDz6qr1H3ZyiPn952zP-FM5zjW8@jackal.rmq.cloudamqp.com/qxbckujb')
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
