from router import *
from keymanager import *
from main import *  


import socket
import threading
import socketserver

from tcpsock import *
from audio import *

zerohash = '00000000'

def forward(self, CHUNK, inkey, outkey):
    while 1:
        send_data(None, receive_data(self, CHUNK, inkey), outkey)

def backward(self, CHUNK,inkey, outkey):
    while 1:
        send_data(self, receive_data(None, CHUNK, outkey), inkey)
        
class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        
        print(self)

        keyHash, sender, target = receive_header(self)
        
        routed = route(host, target)
        data = b'justnotempty'

        
        if G.edge[self.client_address[0]][host]['safe'] == False:
            inkeyData = get_key_byhash(keyHash)
        else:
            inkeyData = None
                
       
        if len(routed) == 1:
            print(sender + '('+keyHash + ')')
                                                           
            
            rcst = Thread(target = read_crypt_send, args = (self, CHUNK, stream, inkeyData,))
            rcwt = Thread(target = rec_crypt_write, args = (self, CHUNK, stream, inkeyData,))
            rcwt.start()
            rcst.start()
            rcwt.join()
            rcst.join()
            
                                                            
        else:
            
            try:
                connect(routed[1])
            except:
                print('connection failed')

            if G.edge[host][routed[1]]['safe'] == False:
                
                key = get_last_key()
                outkeyData = key[1]
                keyHash = key[0]
                
                print(sender + '('+keyHash + ')' + ' - транзитные данные. Целевой IP: ' + target)        
                send_header(keyHash, sender, target)
                
            else:
                outkeyData = None
                send_header(zerohash, sender, target)
                
                
            ft = Thread(target=forward, args =(self, CHUNK, inkeyData, outkeyData,))
            bt = Thread(target=backward, args =(self, CHUNK, inkeyData, outkeyData,))
            bt.start()
            ft.start()
            bt.join()
            ft.join()
            
                        
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

stream = audio_setup()

host = get_ip()
port = G.node[host]['port']
print('My IP: '+ host)

server = ThreadedTCPServer((host, port), ThreadedTCPRequestHandler)
server_thread = threading.Thread(target=server.serve_forever)
server_thread.daemon = False
server_thread.start()
print("Server loop running in thread:", server_thread.name)

target = input("Введите адрес либо пустую строку для ожидания подключения: ")

if target:
    first_transfer(target, stream)
else:
    print('Ожидаем подключения...')
    
    


    
    
        
        
        
        
        
