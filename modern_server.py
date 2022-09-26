import socketserver # simplier than socket in theory

class TCPHandler(socketserver.BaseRequestHandler):
    # override handle method
    def handle(self) -> None:
        return super().handle()

if __name__ == "__main__":
    HOST, PORT = "localhost", 6666

    with socketserver.TCPServer((HOST, PORT), TCPHandler) as my_tcp_server :
        my_tcp_server.serve_forever()