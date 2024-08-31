#!/usr/bin/env python3
import pika

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)



connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')


result = channel.queue_declare(queue='rpc_queue_server', durable=True)
queue_name = result.method.queue
binding_key = "key1.key2.#"
# must be used when used exhanges
channel.queue_bind(
        exchange='topic_logs', queue=queue_name, routing_key=binding_key)



def on_request(ch, method, props, body):
    n = int(body)

    print(f" [.] fib({n})")
    response = fib(n)

    ch.basic_publish(exchange='', routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

    

channel.basic_qos(prefetch_count=1)
channel.basic_consume(
    queue=queue_name, on_message_callback=on_request, auto_ack=False)

print(' [*] Waiting for logs in server ')

channel.start_consuming()