import subprocess
import socket
def run_command(command):
    command=command.rstrip()
    print(command)
    try:
        child = subprocess.run(command,shell=True)
    except:
        child = "对不起并没有这个命令"
    return child
socket_object = socket.socket()
socket_object.bind(("127.0.0.1",2345))
socket_object.listen(5)
str="hello world"
while True:
    conn,address = socket_object.accept()
    print("a new connect from",address)
    conn.send(str.encode(encoding='gbk'))
    data=conn.recv(1024)
    data=bytes.decode(data)
    print("the command is" + data) 
    output = run_command(data)
    print(output)
conn.close()