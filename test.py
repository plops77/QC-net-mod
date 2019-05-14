from router import *
from keymanager import *
from main import *  
from threading import Thread


import socket
import threading
import socketserver

from tcpsock import *

from audio import *

zerohash = '00000000'


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    

    def handle(self):
        data = b'justnotempty'
        


        def sen():
            while 1:
                send_data(self, stream.read(CHUNK), None)
        
        def rec():
            while 1:
                stream.write(receive_data(self, CHUNK, None))

        rt = Thread(target = rec)
        st = Thread(target = sen)
        rt.start()
        st.start()
        rt.join()
        st.join()
        
            
            


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


stream = audio_setup()


server = ThreadedTCPServer((get_ip(), 60001), ThreadedTCPRequestHandler)
server_thread = threading.Thread(target=server.serve_forever)

server_thread.daemon = True

server_thread.start()
print("Server loop running in thread:", server_thread.name)

target = input("Введите адрес либо пустую строку для ожидания подключения: ")



def first_transfer(target, stream):

    def sen():
            while 1:
                send_data(None, stream.read(CHUNK), None)
        
    def rec():
        while 1:
            stream.write(receive_data(None, CHUNK, None))

    rt = Thread(target = rec)
    st = Thread(target = sen)
    rt.start()
    st.start()
    rt.join()
    st.join()

if target:
    connect(target)
    first_transfer(target, stream)
else:
    pass
    


    
    
        
        
        
        
        
