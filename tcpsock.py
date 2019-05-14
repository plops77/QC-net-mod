import socket                   # Import socket module
from router import *
from keymanager import crypt


s = socket.socket()             # Create a socket object

def connect(host):
    port = G.node[host]['port']    
    try:
        s.connect((host, port))
    except: print('Абонент не доступен')

def send_header(keyHash, sender, target):
    s.send(keyHash.encode())
    s.send(strip_tobytes(sender))
    s.send(strip_tobytes(target))

def send_data(handler, data, key):
    
    if key:
        if handler:
            handler.request.send(crypt(data, key))
        else:
            s.send(crypt(data, key))

    else:
        if handler: 
            handler.request.send(data)
        else:
            s.send(data)
        

def receive_header(handler):
    keyHash = handler.request.recv(8).decode() #receive hash
    print(keyHash)
    sender = bytesip_tostr(handler.request.recv(4)) #receive sender's IP
    print(sender)
    target = bytesip_tostr(handler.request.recv(4)) #receive target's IP
    print(target)
    
    return keyHash, sender, target
    
def receive_data(handler, CHUNK, key):
    if handler:
        
        data = handler.request.recv(CHUNK)
    else:
       
        data = s.recv(CHUNK)
    if key:
        return crypt(data, key)
    else:
        return data
   

    
