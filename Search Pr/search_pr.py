import socket
import S5Crypto
from bot import *
    
def search_pr_i(username,cfg):
    msg_start = '🛰️ Buscando proxy🛰️'       
    range_min = cfg[username]['range_min']
    range_max = cfg[username]['range_max']
    ip = cfg[username]['ip']
    msg_status = f'{msg_start}\n\n➖R_Min: {range_min}\n➕R_Max: {range_max}\n🌐Ip: {ip}'   
    print("Buscando proxy...")
    for port in range(int(range_min),int(range_max)):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        result = sock.connect_ex((ip,port))  

        if result == 0: 
            print ("Puerto abierto!")
            print (f"Puerto: {port}")  
            proxy = f'{ip}:{port}'
            proxy_new = S5Crypto.encrypt(f'{proxy}')
            msg = '🥳🎇Enhorabuena🎇🥳:\n🛰️Proxy Encontrado 🛰️\n\n🌐Ip+Puerto: '+proxy+'\nsocks5://' + proxy_new
            break
        else:             	                
            print ("Error...Buscando...")                
            print (f"Buscando en el puerto: {port}")
            sock.close()
         
    return