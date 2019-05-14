import networkx as nx
#import matplotlib.pyplot as plt



def get_ip():
    import socket
    ip = socket.gethostbyname(socket.gethostname())
##    localIP = '192.168.0.100'     #local IP available to connect
##    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
##    s.connect((localIP, 0))
##    ip = s.getsockname()[0]
##    s.close()
    return ip

def route(sourceIP, targetIP):
    
    return nx.shortest_path(G, source = sourceIP, target = targetIP)
    
    
def strip_tobytes(strip):
    strip = strip.split('.')
    result=[]
    for sign in strip:
        result.append(int(sign))
    return bytes(result)

def bytesip_tostr(bytesip):
    ip = memoryview(bytesip).tolist()
    result=''
    for sign in ip:
        result+=str(sign)+'.'
    return result[:-1]
    
G = nx.Graph()
G.add_nodes_from([#('10.0.8.164', {'port' : 60001}),
                  ('10.0.8.168', {'port' : 60001}),
                  #('10.8.11.41', {'port' : 60001}),
                  #('10.8.11.11', {'port' : 60001}),
                  ('10.8.11.7' , {'port' : 60001}),
                  #('10.8.11.43', {'port' : 60001}),
                  
                  ])
                  



G.add_edges_from([#('10.0.8.164', '10.8.11.11', {'safe' : False}),
                  #('10.0.8.168', '10.8.11.43', {'safe' : False}), 
                  #('10.8.11.41', '10.8.11.7', {'safe' : False}),
                  #('10.8.11.11', '10.8.11.43', {'safe' : True}),
                  #('10.8.11.11', '10.8.11.7', {'safe' : True}),
                  #('10.8.11.7', '10.8.11.43', {'safe' : True}),
                  ('10.0.8.168', '10.8.11.7', {'safe' : False}), 
                  ])

