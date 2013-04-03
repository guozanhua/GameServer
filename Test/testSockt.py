#!/usr/bin/python

from socket import *


sock = socket(AF_INET,SOCK_STREAM)
sock.connect(('112.95.238.67',806))
sock.send('fuck')
print sock.recv(1024)
sock.close()
