import glob, os
import sys
from pathlib import Path
import numpy as np
import random as rn
from audio import CHUNK

keyDir ='C:\\Users\\XE\\Desktop\\Архив в Казань\\kks2_stream\\project\\test\\kks1\\exe\\keys'

def get_last_key():
    
    dirList = Path(keyDir).glob('*.key')
    keyAddr = str(next(dirList))

    #print(keyAddr)
    slashPos = keyAddr.rindex('\\')+1
    
    keyHash = keyAddr[slashPos:slashPos+8]
    
    keyData = open(keyAddr, 'rb').read()
    
    os.remove(keyAddr)
   
    return keyHash, keyData
    

def get_key_byhash(keyHash):
    try:
        keyAddr = glob.glob(keyDir + '\\' + keyHash + '*.key')[0]
        keyData = open(keyAddr, 'rb').read()
        os.remove(keyAddr)
    except:
        print('Требуемый ключ '+keyHash+' не найден.')
    
    return keyData
    

def crypt(data, key):
    result=[]
    key = key[8:]
    i=0    
    for byte in data:
        if i==len(key): i=0
        result.append(np.bitwise_xor(byte, 170))
        i+=1
       
    return bytes(result)

        
        



