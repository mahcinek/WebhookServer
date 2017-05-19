from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import time
from random import randint


class SimpleEcho(WebSocket):

    def handleMessage(self):
        # echo message back to client

            time.sleep(randint(0,3))
            value=str(randint(5,29))
            print value
            self.sendMessage(value)


    def handleConnected(self):
        print(self.address, 'connected')
        self.sendMessage(str(randint(5,29)))



    def handleClose(self):
        print(self.address, 'closed')

server = SimpleWebSocketServer('', 8000, SimpleEcho)
server.serveforever()