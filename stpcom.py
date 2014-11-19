#!/usr/bin/python
from logging.handlers import TimedRotatingFileHandler   
import logging   
import os   
import stomp
import sys
import time
  
  
# def initLogger(logFileName):   
#         if not os.path.isfile(logFileName):   
#             logPath = logFileName[0:logFileName.rfind('/') + 1]   
#             if not os.path.isdir(logPath):   
#                 os.makedirs(logPath)   
#             f = open(logFileName, 'w')   
#             f.close()   
#         format = '%(asctime)s [%(threadName)s](%(levelname)s) %(pathname)s(%(funcName)s:%(lineno)s) --> %(message)s'  
#         filemode = 'a'  
#         # level = logging.DEBUG   
#         level = logging.INFO   
#         logging.basicConfig(filemode=filemode, level=level, format=format)   
#         hdlr0 = TimedRotatingFileHandler(logFileName, when='D', interval=1, backupCount=0, encoding='utf-8', delay=False, utc=False)   
#         formatter = logging.Formatter(format)   
#         hdlr0.setFormatter(formatter)   
#         logger = logging.getLogger()   
#         logger.addHandler(hdlr0)   
#         return logger   
  
  
# logger = initLogger('./logs/simple.log')   
  
class MyListener(object):   
    def on_error(self, headers, message):   
        print('received an error %s' % message)   
    def on_message(self, headers, message):
        print "aaa"
        print('----->received a message %s' % message) 
  
def main():            
    dest = '/queue/inbox'  
       
    conn = stomp.Connection(host_and_ports=[('127.0.0.1', 61612) ])   
    conn.set_listener('listen1', MyListener())   
    conn.start()   
    conn.connect()   
    conn.subscribe(destination=dest, id=1, ack='auto')
    print "waiting for a message"
    while 1:
        time.sleep(10)
    # while num < 2:   
    #     conn.send(body=msg, destination=dest)   
    #     print 'send message ', msg   
    #     num = num + 1    
       
  
if __name__ == '__main__':   
    main()  
