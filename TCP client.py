import socket 
host = "127.0.0.1"
port = 9998
def client_TCP(host,port):
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 将客户端连接到服务器
    client.connect((host,port))
    # 向服务端发送数据 必须是bytes
    client.send(b"wjkwf")
    # 接受服务端的消息
    date = client.recv(4096)
    # 输出socket decode解码
    print(date.decode())
    # 关闭socket
    client.close()
    