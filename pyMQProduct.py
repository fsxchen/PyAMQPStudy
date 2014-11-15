<<<<<<< HEAD
import pika, os, urlparse, logging
logging.basicConfig()

# Parse CLODUAMQP_URL (fallback to localhost)
url_str = os.environ.get('CLOUDAMQP_URL', 'amqp://qjlyybjx:LePPUNrXTDaZ-BKBj2tLcDkxeMkLaH0W@turtle.rmq.cloudamqp.com/qjlyybjx')
url = urlparse.urlparse(url_str)
params = pika.ConnectionParameters(host=url.hostname, virtual_host=url.path[1:],
    credentials=pika.PlainCredentials(url.username, url.password))

connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue
# send a message
channel.basic_publish(exchange='', routing_key='hello', body='Hello CouCou!')
print " [x] Sent 'Hello World!'"

# create a function which is called on incoming messages
# def callback(ch, method, properties, body):
#   print " [x] Received %r" % (body)

# # set up subscription on the queue
# channel.basic_consume(callback,
#     queue='hello',
#     no_ack=True)

# channel.start_consuming() # start consuming (blocks)

# connection.close()
=======
#!/usr/bin/env python
#coding:utf-8
import pika, os, urlparse

import json

test = {
    "id": 1,
    "ip": '192.168.1.254',
    "packet_id": 60,
    "packet_size": 0,
    "script_start_time": '',
    "script_end_time": '',
    "result": '',
    "res_enctypes": 0,
    "sent_time": '',
    "recv_time": '',
    "res_type": 0
}

test_str = json.dumps(test)

try:
    eval(URL)
except NameError, e:
    from pyMQConsum import URL, connect2ser

def sentMessage(ch, queueName="hello", body="hello amqp"):
    ch.queue_declare(queue=queueName) 
    ch.basic_publish(exchange='', routing_key=queueName, body=body)
    print " [x] Sent 'Hello World!'"
    ch.close()

if __name__ == '__main__':
    ch = connect2ser(URL)
    sentMessage(ch, body=test_str)
>>>>>>> e1e3a05f8be658bb3e707c30b409c73a0d281553
