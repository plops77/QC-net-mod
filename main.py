from audio import *

from tcpsock import *
from router import *
from keymanager import *

from threading import Thread, Event

zerohash = '00000000'



def read_crypt_send(self, CHUNK, stream, key):
    while 1:
        send_data(self, stream.read(CHUNK), key)
        
        
def rec_crypt_write(self, CHUNK, stream, key):
    while 1:
        stream.write(receive_data(self, CHUNK, key))

            
def first_transfer(target, stream):
    
    
    routed = route(get_ip(), target)
    sender = routed[0]

    try:
        connect(routed[1])
    except:
        print('connection failed')

    if G.edge[routed[0]][routed[1]]['safe'] == False:

        key = get_last_key()
       
        keyData = key[1] 
        keyHash = key[0]  

        print(keyHash)     
        
        send_header(keyHash, sender, target)

               
    else:
        keyData = None
        send_header(zerohash, sender, target)
        
    rcst = Thread(target = read_crypt_send, args = (None, CHUNK, stream, keyData))
    rcwt = Thread(target = rec_crypt_write, args = (None, CHUNK, stream, keyData))    
        

    rcst.start()
    rcwt.start()
    rcst.join()
    rcwt.join()
            

    
    

   
