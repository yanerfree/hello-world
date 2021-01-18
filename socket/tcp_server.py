import socket

ip_port = ("127.0.0.1",8808)
back_log = 5
buffer_size = 1024
#1、创建TCP 套接字
#sock=socket.socket()
tcp_ser = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   # 套接字类型AF_INET, socket.SOCK_STREAM   tcp协议，基于流式的协议
tcp_ser.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  # 对socket的配置重用ip和端口号
#2、绑定ip端口号
tcp_ser.bind(ip_port)
#3、设置半连接池，最多可以连接几个客户端
tcp_ser.listen(back_log)

count = 0
while 1:
    print("server waiting.....")
    #4、阻塞等待，监听端口
    conn,addr=tcp_ser.accept()
    count += 1
    print("connect 【%s】 times, From %s"%(count,addr))
    #接收信息
    while 1:
        try:
            msg = conn.recv(buffer_size)
            print('msg:%s'%msg.decode('utf-8'))
            
            if msg.decode('utf-8') == 'END':
                res = 'OK'
                conn.send(res.encode('utf-8'))# 收发消息一定要二进制，记得编码
                conn.close()#断开连接
                print('断开连接...')
                break
         
        except Exception as e:
            print(e)
            break

    # 读取html文件
    '''
    with open("login.html","rb") as f:
        data=f.read()
    conn.send((b"HTTP/1.1 200 OK\r\n\r\n%s"%data))
    conn.close()
    '''
tcp_ser.close()# 关闭服务器    
