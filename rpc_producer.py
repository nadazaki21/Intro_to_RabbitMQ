#!/usr/bin/env python3
import pika
import uuid


class FibonacciRpcClient(object):

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))

        self.channel = self.connection.channel()

        # the callback channel to receivethe response that is different from the  publishing channel 

        call_back_queue = self.channel.queue_declare(queue='call_back_queue', exclusive=True)
        self.callback_queue = call_back_queue.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

        self.response = None
        self.corr_id = None
        self.routing_key = "key1.key2.nada"

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body
    
    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())

        self.channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

        self.channel.basic_publish(
        exchange='topic_logs', routing_key= self.routing_key, body=str(n),
        properties=pika.BasicProperties(
        delivery_mode=pika.DeliveryMode.Persistent,
        reply_to=self.callback_queue,
        correlation_id=self.corr_id))
        
        while self.response is None:
            self.connection.process_data_events(time_limit=None)
        return int(self.response)
        

        


fibonacci_rpc = FibonacciRpcClient()

print(" [x] Requesting fib(30)")
response = fibonacci_rpc.call(30)
print(f" [.] Got {response}")





