from socket import *

ip_port = ("127.0.0.1",8808)
buffer_size = 1024

udp_ser = socket(AF_INET, SOCK_DGRAM)  # 数据报式的套接字
udp_ser.bind(ip_port)

count = 0
while 1:
    print("server waiting.....")
    #data = udp_ser.recvfrom(buffer_size)
    #print('data:',data)#recefrom() 接受的结果是发送的信息，和发送方的IP和端口号
    #接收数据
    msg,addr = udp_ser.recvfrom(buffer_size)
    count += 1
    print('Msg【%s】:%s, From:%s'%(count,msg.decode('utf-8'),addr))
    #回复
    udp_ser.sendto('OK'.encode('utf-8'), addr)
    
    
udp_ser.close()