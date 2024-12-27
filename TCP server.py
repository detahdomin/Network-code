import socket
import threading

IP = "0.0.0.0"
port = 9998



def main():
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 将套接字绑定到socket套接字必须尚未绑定
    server.bind((IP,port))
    # 启动一个服务器用于接受连接
    server.listen(5)
    print(f'[*]listening on {IP}:{port}')
    while True:
        # 接受一个连接。此 socket 必须绑定到一个地址上并且监听连接。返回值是一个 (conn, address) 对
        # 其中 conn 是一个 新 的套接字对象，用于在此连接上收发数据，address 是连接另一端的套接字所绑定的地址。
        client,address = server.accept()
        print(f"Accepted connection from{address[0]}:{address[1]}")
        # 创建线程对象
        client_handler = threading.Thread(target=handle_client, args=(client,))
        # 开始线程
        client_handler.start()



def handle_client(client_socket):
    # 上下文管理器 自动创建一个对象 开始后会关闭
    with client_socket as sock:
        # 从套接字接收数据。返回值是一个字节对象，表示接收到的数据。
        request = sock.recv(1024)
        print(f'[*] Received:{request.decode("utf-8")}')
        # 发送bytes数据给客户端，由客户端进行解码
        sock.send(b'ACK')


        
if __name__=='__main__':
    main()