import socket
str_msg = input("请输入要发送的信息")
socket_object = socket.socket()
socket_object.connect(("127.0.0.1",2345))
str_msg = str_msg.encode(encoding='gbk')
socket_object.send(str_msg)
print(str(socket_object.recv(1024)))
socket_object.close()