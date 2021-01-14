from socket import *

ip_port = ("127.0.0.1",8808)
buffer_size = 1024

udp_client = socket(AF_INET, SOCK_DGRAM)  # 数据报式的套接字

while 1:
    msg = input('please input:\r\n')
    udp_client.sendto(msg.encode('utf-8'),ip_port)
    
    res,addr = udp_client.recvfrom(buffer_size)
    
    print('Res:%s, From:%s'%(res.decode('utf-8'),addr))
    
    
s.close()