#!/usr/bin/env python
#coding:utf-8

import pika, os, urlparse, json
import socket

URL = ''
TIMEOUT = 10
INFODICT = {
    "id": 0,
    "ip": '',
    "packet_id": 0,
    "packet_size": 0,
    "script_start_time": '',
    "script_end_time": '',
    "result": '',
    "res_enctypes": 0,
    "sent_time": '',
    "recv_time": '',
    "res_type": 0
}

socket.timeout = TIMEOUT

def connect2ser(url):
    url_str = os.environ.get('CLOUDAMQP_URL', url)
    url = urlparse.urlparse(url_str)
    params = pika.ConnectionParameters(host=url.hostname, virtual_host=url.path[1:],
        credentials=pika.PlainCredentials(url.username, url.password))
    connection = pika.BlockingConnection(params) # Connect to CloudAMQP
    channel = connection.channel()
    return channel

def consum(channel, queueName='hello'):
    channel.basic_consume(callback,queue=queueName,no_ack=True)
    channel.start_consuming()

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body)
    revd_info = json.loads(body)
    if revd_info["id"] == 1:
        ip = revd_info["ip"]
        isAlive(ip, port)

def isAlive(ip, port):
    HELLO = "hello\n"
    try:
        socket = socket.socket()
        socket.connect((ip, port))
        socket.send(HELLO)
        rec_data = socket.recv(1024)
        if rec_data.strip() == "OK":
            return True
    except Exception, e:
        print e
        return False


def main():
    ch = connect2ser(URL)
    consum(ch)
    print "hello coucou"

isAlive("127.0.0.1", 80)

# if __name__ == '__main__':
#     main()