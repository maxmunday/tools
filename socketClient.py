#!/usr/bin/python
# HTTP Client with Socket
# www.maxmunday.com

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("vulnerable" , 80))

s.sendall("GET /\r\n")
print s.recv(4096)

s.close
