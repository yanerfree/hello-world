import socket

ip_port = ("127.0.0.1",8808)
buffer_size = 1024

tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_client.connect(ip_port)

while 1:
    msg = input('please input:\r\n')
    #防止输入空消息
    #if not msg :
        #continue
    tcp_client.send(msg.encode('utf-8'))
    
    if msg == 'END':
        break
        
res = tcp_client.recv(buffer_size)
print('res:%s'%res.decode('utf-8'))
print('通话结束')