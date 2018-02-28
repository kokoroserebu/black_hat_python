# -*- conding: utf-8 -*-

import socket

target_host = "221.251.190.130"
target_port = 8441


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


client.connect((target_host,target_port))


client.send("happy birthday!")


response = client.recv(4096)

print(response)