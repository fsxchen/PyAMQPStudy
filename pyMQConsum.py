#!/usr/bin/env python
#coding:utf-8

import pika
import pika, os, urlparse, logging
logging.basicConfig()

# Parse CLODUAMQP_URL (fallback to localhost)
url_str = os.environ.get('CLOUDAMQP_URL', 'amqp://aaa:bbb@x.x.x./xxx')
url = urlparse.urlparse(url_str)
params = pika.ConnectionParameters(host=url.hostname, virtual_host=url.path[1:],
    credentials=pika.PlainCredentials(url.username, url.password))

connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel
# channel.queue_declare(queue='hello') # Declare a queue
# send a message
# channel.basic_publish(exchange='', routing_key='hello', body='Hello CloudAMQP!')

# create a function which is called on incoming messages
def callback(ch, method, properties, body):
  print " [x] Received %r" % (body)

# set up subscription on the queue
channel.basic_consume(callback,
    queue='hello',
    no_ack=True)

channel.start_consuming() # start consuming (blocks)

connection.close()
