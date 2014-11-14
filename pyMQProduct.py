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