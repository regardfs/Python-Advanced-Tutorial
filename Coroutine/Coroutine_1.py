#!/usr/bin/env python
import time

def consumer():
    r = ''
    while True:
        print "[CONSUMER] r:%s" % r
        n = yield r
        print "[CONSUMER] n:%s" % n
        if not n:
            print "[CONSUMER] if not n:%s" % n
            return
        print('[CONSUMER] Consuming %s...' % n)
        time.sleep(1)
        r = '200 OK'

def produce(c):
    c.next()
    n = 0
    while n < 5:
        n = n+1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

if __name__=='__main__':
    c = consumer()
    produce(c)