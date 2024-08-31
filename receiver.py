#!/usr/bin/env python3
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')


# result = channel.queue_declare('', exclusive=True)
result = channel.queue_declare(queue='task_queue', durable=True)
queue_name = result.method.queue

binding_key = "key1.key2.#"


channel.queue_bind(
        exchange='topic_logs', queue=queue_name, routing_key=binding_key)



print(' [*] Waiting for logs ***in Q1***. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(f" [x] ***in Q1*** {method.routing_key}:{body}")
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=False)


channel.start_consuming()