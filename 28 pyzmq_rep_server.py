
import zmq
import time

localhost = '127.0.0.1'
port = '5555'

def run_server():
    print('Start to bind server... {} {}'.format(localhost, port))
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind('tcp://{}:{}'.format(localhost, port))
    poller = zmq.Poller()
    poller.register(socket, zmq.POLLIN)
    while True:
        socks = dict(poller.poll(timeout=0.05))
        if socks.get(socket) == zmq.POLLIN:
            message = socket.recv()
            # more = self.socket_rep.getsockopt(zmq.RCVMORE)
            print('Recieved request: [ %s ]' % message)
            socket.send('recv OK')
        time.sleep(0.05)
    socket.close()

if __name__ == '__main__':
    run_server()