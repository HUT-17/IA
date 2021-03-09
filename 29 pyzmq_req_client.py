#!/usr/bin/env python
#-*- conding:utf-8 -*-
import zmq
import time

localhost = '127.0.0.1'
port = '5555'

def run_client():
    context = zmq.Context()
    #  Socket to talk to server
    print('Connecting to server... {} {}'.format(localhost, port))
    socket = context.socket(zmq.REQ)
    socket.connect('tcp://{}:{}'.format(localhost, port))

    # Do 10 requests, waiting each time for a response
    for request in range(10):
        print('Sending request {}'.format(request))
        socket.send('Hello {}'.format(request))
        #  Get the reply.
        message = socket.recv()
        print('Received reply {} [ {} ]'.format(request, message))
        time.sleep(1)

if __name__ == '__main__':
    run_client()