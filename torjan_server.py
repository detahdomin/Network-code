import socketserver
class MyTCPhandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            while True:
                self.data = self.request.recv(1024)
                cmd = input("(quit 退出>>").strip()
                if len(cmd) == 0:
                    continue
                if cmd == "quit":
                    break
                if not self.data:
                    print("connection lost")
                    break
                print(self.data.decode())
                self.request.sendall(cmd.encode())
        except Ellipsis as e:
            print(self.address,"连接断开")
        finally:
            self.request.close()
    def setup(self):
        print("before handle,连接建立:",self.client_address)
    def finish(self):
        print("finsh run after handle")
if __name__=="__main__":
    HOST,PORT = "localhost",9999
    sever = socketserver.TCPServer((HOST,PORT),MyTCPhandler)
    sever.serve_forever()