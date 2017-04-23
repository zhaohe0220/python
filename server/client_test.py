#!/user/bin/python
# -*- coding: UTF-8 -*-

import socket

c=socket.socket()
host=socket.gethostname()
port=1234
c.connect((host,port))

print c.recv(1024)
c.close()