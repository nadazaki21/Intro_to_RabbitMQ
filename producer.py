#!/usr/bin/env python3
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Topic 
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

routing_key = "key3.hi.nada"


msg = "Testing..."

channel.basic_publish(
    exchange='topic_logs', routing_key= routing_key, body= msg,
    properties=pika.BasicProperties(
        delivery_mode=pika.DeliveryMode.Persistent
        
    )
)

connection.close()