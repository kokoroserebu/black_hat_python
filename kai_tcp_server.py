import socket
from datetime import datetime
from time import sleep

server_socket = socket.socket()

port = 5000
server_socket.bind(('', port))

while True:
    print "[*] Listening on %s" % (port)
    server_socket.listen(5)
    client, addr = server_socket.accept()
    print "[*] Accepted connection from: %s:%d:%s" % (addr[0],addr[1],client)
    print(client.recv(4096))
    while True:
        print('sending')
        now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        try:
            client.send(now)
        except:
            break
        sleep(1)
    client.close()
server_socket.close()